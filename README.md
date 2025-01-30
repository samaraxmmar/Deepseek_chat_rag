

<span style="font-size: 36px; color: blue;">DeepSeek</span> Chat RAG

DeepSeek Chat RAG is a project that utilizes advanced retrieval-augmented generation (RAG) models to answer user queries based on documents. The system extracts and indexes content from various file formats (PDF, DOCX, CSV, etc.), storing the data in a Chroma database. It then uses this information to provide relevant answers to user queries using a conversational model.

## Features

- **Document Extraction:** Supports PDF, DOCX, TXT, and CSV formats.
- **Document Indexing:** Text extracted from documents is indexed in a Chroma database for efficient retrieval.
- **Question Answering:** Uses the RAG model to answer user questions based on the indexed documents.
- **Groq Integration:** Powered by Groq's LLM for enhanced response generation.

## Requirements

- Python 3.8+
- The following libraries (installed via `requirements.txt`):
  - `langchain`
  - `langchain-community`
  - `langchain-huggingface`
  - `langchain-chroma`
  - `langchain-groq`
  - `fitz` (PyMuPDF)
  - `pandas`
  - `docx`
  
## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/samaraxmmar/Deepseek_chat_rag.git
    cd Deepseek_chat_rag
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv my_env
    source my_env/bin/activate   # On Windows: my_env\Scripts\activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Add Documents:** Place your documents (PDF, DOCX, etc.) in the project folder.
2. **Run the Document Processing:**
   - To process and index the documents, use the following command:
     ```bash
     python streamlit_chat.py
     ```
3. **Ask Questions:** After indexing, you can query the system to receive answers based on the documents.
   - Example:
     ```bash
     python streamlit_chat.py "What is the impact of Groq's LLM?"
     ```

## Contributing

Feel free to fork the repository and create a pull request with any improvements, fixes, or features.



