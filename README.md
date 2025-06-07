# DeepSeek RAG Chatbot 🤖

<p align="center">
  <img src="https://user-images.githubusercontent.com/74038190/219923831-5843447c-1748-423c-9118-24989e226165.png" alt="DeepSeek RAG Chatbot Banner" width="700">
</p>

<p align="center">
    <b>An intelligent chatbot powered by Groq, LangChain, and ChromaDB to chat with your documents.</b>
<br/><br/>
    <a href="https://github.com/samaraxmmar/Deepseek_chat_rag/issues"><img src="https://img.shields.io/github/issues/samaraxmmar/Deepseek_chat_rag?style=for-the-badge&color=brightgreen" alt="Issues"></a>
    <a href="https://github.com/samaraxmmar/Deepseek_chat_rag/stargazers"><img src="https://img.shields.io/github/stars/samaraxmmar/Deepseek_chat_rag?style=for-the-badge&color=f0c60f" alt="Stars"></a>
    <a href="https://github.com/samaraxmmar/Deepseek_chat_rag/blob/main/LICENSE"><img src="https://img.shields.io/github/license/samaraxmmar/Deepseek_chat_rag?style=for-the-badge&color=blue" alt="License"></a>
</p>

---

## 🌟 Introduction

**DeepSeek RAG Chatbot** is a powerful and intuitive application that allows you to have conversations with your own documents. By leveraging the speed of the **Groq LPU Inference Engine** and the versatility of **LangChain**, this tool transforms your static files (PDFs, DOCX, TXT, CSV) into an interactive knowledge base.

Simply upload your documents, and the system will automatically process, index, and prepare them for your questions. The user-friendly interface, built with **Streamlit**, makes it easy for anyone to get instant, accurate answers drawn directly from the provided content.

## ✨ Key Features

* **Multi-Format Document Support**: Upload and process various file types, including `.pdf`, `.docx`, `.txt`, and `.csv`.
* **High-Speed Inferencing**: Powered by **Groq**, delivering responses at exceptional speed for a fluid, real-time conversational experience.
* **Advanced RAG Pipeline**: Utilizes **LangChain** for robust Retrieval-Augmented Generation, ensuring answers are relevant and contextually accurate.
* **Efficient Vector Storage**: Employs **ChromaDB** to create and manage a persistent vector database of your document embeddings for fast retrieval.
* **User-Friendly Interface**: A clean and simple web UI built with **Streamlit** that includes real-time processing feedback and chat history.
* **Open Source & Customizable**: Fully open-source, allowing for easy customization and integration into other projects.

## ⚙️ How It Works

The application follows a sophisticated Retrieval-Augmented Generation (RAG) architecture to provide answers from your documents.

<p align="center">
  <img src="[https://i.imgur.com/A8O1Z9B.png](https://www.google.com/imgres?q=RAG%20Architecture%20Diagram&imgurl=https%3A%2F%2Fwww.deepchecks.com%2Fwp-content%2Fuploads%2F2024%2F10%2Fimg-rag-architecture-model.jpg&imgrefurl=https%3A%2F%2Fwww.deepchecks.com%2Fglossary%2Frag-architecture%2F&docid=77NHblHjJBDcLM&tbnid=tAnnhoVChABTzM&vet=12ahUKEwjLnqut7N-NAxXW_rsIHUhsGNQQM3oECGYQAA..i&w=680&h=346&hcb=2&ved=2ahUKEwjLnqut7N-NAxXW_rsIHUhsGNQQM3oECGYQAA)" alt="RAG Architecture Diagram" width="700">
</p>

1.  **Document Loading**: You upload your documents (PDF, DOCX, etc.) through the Streamlit interface.
2.  **Text Splitting & Embedding**: The system loads the documents, splits them into smaller, manageable chunks, and generates vector embeddings for each chunk.
3.  **Vector Indexing**: These embeddings are stored in a **ChromaDB** vectorstore, creating a searchable index of your document's knowledge.
4.  **User Query**: You ask a question in the chat interface.
5.  **Context Retrieval**: The system takes your query, embeds it, and performs a similarity search in ChromaDB to retrieve the most relevant document chunks (the "context").
6.  **Response Generation**: The retrieved context and your original query are passed to the **Groq**-powered language model, which generates a human-like, accurate answer based on the provided information.

## 🚀 Getting Started

Follow these steps to set up and run the project on your local machine.

### Prerequisites

* Python 3.8+
* A Groq API Key. You can get one for free at [GroqCloud](https://console.groq.com/keys).

### 1. Clone the Repository

```bash
git clone [https://github.com/samaraxmmar/Deepseek_chat_rag.git](https://github.com/samaraxmmar/Deepseek_chat_rag.git)
cd Deepseek_chat_rag
