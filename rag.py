import os
import json
import logging
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from docx import Document  # Pour les fichiers DOCX
import fitz  # PyMuPDF pour les PDFs
import pandas as pd  # Pour les CSV


# Configuration du logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Définition du répertoire de travail
working_dir = os.path.dirname(os.path.abspath(__file__))

# Charger les configurations
try:
    with open(os.path.join(working_dir, "config.json")) as config_file:
        config_data = json.load(config_file)
        GROQ_API_KEY = config_data.get("GROQ_API_KEY", "")
except Exception as e:
    logging.error(f"Erreur de chargement du fichier config.json: {e}")
    raise

os.environ["GROQ_API_KEY"] = GROQ_API_KEY

# Chargement du modèle d'embedding
embedding = HuggingFaceEmbeddings()

# Chargement du modèle LLM de Groq
llm = ChatGroq(
    model="deepseek-r1-distill-llama-70b",
    temperature=0
)


def extract_text(file_path, file_type):
    """ Extrait le texte d'un fichier en fonction de son type """
    text = ""
    try:
        if file_type == "pdf":
            doc = fitz.open(file_path)
            for page in doc:
                text += page.get_text()
        elif file_type == "docx":
            doc = Document(file_path)
            for para in doc.paragraphs:
                text += para.text + "\n"
        elif file_type == "txt":
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()
        elif file_type == "csv":
            df = pd.read_csv(file_path)
            text = df.to_string()
        else:
            logging.warning(f"Format non supporté: {file_type}")
    except Exception as e:
        logging.error(f"Erreur de lecture du fichier {file_path}: {e}")

    return text


def process_document_to_chroma_db(file_name):
    # load the doc using unstructured
    loader = UnstructuredPDFLoader(f"{working_dir}/{file_name}")
    documents = loader.load()
    # splitting te text into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000,
        chunk_overlap=200
    )
    texts = text_splitter.split_documents(documents)
    vectordb = Chroma.from_documents(
        documents=texts,
        embedding=embedding,
        persist_directory=f"{working_dir}/doc_vectorstore"
    )
    return 0

def answer_question(user_question):
    # load the persistent vectordb
    vectordb = Chroma(
        persist_directory=f"{working_dir}/doc_vectorstore",
        embedding_function=embedding
    )
    # retriever
    retriever = vectordb.as_retriever()

    # create a chain to answer user question usinng DeepSeek-R1
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
    )
    response = qa_chain.invoke({"query": user_question})
    answer = response["result"]

    return answer
