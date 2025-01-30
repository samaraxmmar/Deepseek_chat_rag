import os
import streamlit as st
from rag_utility import process_document_to_chroma_db, answer_question
import fitz  # PyMuPDF pour lire les PDFs
from docx import Document  # Pour les fichiers DOCX
import pandas as pd  # Pour les fichiers CSV

# Définir le répertoire de travail
working_dir = os.getcwd()

# Personnalisation de l'interface Streamlit
st.set_page_config(page_title="Chatbot avec RAG", layout="wide")
st.title("🤖 Chatbot Intelligent avec DeepSeek-R1")
st.markdown("---")

# Initialiser l'historique des messages
if "history" not in st.session_state:
    st.session_state.history = []

# Zone de chat interactive et upload de fichier
st.subheader("💬 Chat avec le modèle DeepSeek-R1")

# Zone de saisie pour la question et upload de fichier
user_input = st.text_input("Posez votre question :", key="user_input")
uploaded_file = st.file_uploader("Importez un document", type=["pdf", "docx", "txt", "csv"])

# Fonction pour extraire du texte en fonction du type de fichier
def extract_text(file, file_type):
    text = ""
    if file_type == "pdf":
        doc = fitz.open(stream=file.read(), filetype="pdf")
        for page in doc:
            text += page.get_text()
    elif file_type == "docx":
        doc = Document(file)
        for para in doc.paragraphs:
            text += para.text + "\n"
    elif file_type == "txt":
        text = file.read().decode("utf-8")
    elif file_type == "csv":
        df = pd.read_csv(file)
        text = df.to_string()
    return text

# Lorsque l'utilisateur clique sur "Envoyer"
if st.button("Envoyer"):
    if user_input:
        response = answer_question(user_input)
        st.session_state.history.append((user_input, response))
    
    # Si un fichier a été téléchargé, on l'analyse et on ajoute son contenu à la base de données
    if uploaded_file is not None:
        file_type = uploaded_file.name.split(".")[-1]
        document_text = extract_text(uploaded_file, file_type)
        file_path = os.path.join(working_dir, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        process_document_to_chroma_db(uploaded_file.name)
        st.success("✅ Document analysé et ajouté à la base de connaissances !")
        
        # Ajouter un aperçu du document
        st.subheader("📖 Aperçu du document :")
        st.text_area("", document_text[:1000], height=250, disabled=True)

# Affichage de l'historique des conversations
for question, answer in st.session_state.history:
    st.markdown(f"**🧑‍💻 Vous :** {question}")
    st.markdown(f"**🤖 DeepSeek-R1 :** {answer}")
    st.markdown("---")
