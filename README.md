DeepSeek RAG Chatbot 🤖
&lt;p align="center">
&lt;img src="[lien suspect supprimé]" alt="DeepSeek RAG Chatbot Banner">
&lt;/p>

&lt;p align="center">
&lt;b>An intelligent chatbot powered by Groq, LangChain, and ChromaDB to chat with your documents.&lt;/b>
&lt;br/>&lt;br/>
&lt;a href="[lien suspect supprimé]">&lt;img src="[lien suspect supprimé]" alt="Issues">&lt;/a>
&lt;a href="[lien suspect supprimé]">&lt;img src="[lien suspect supprimé]" alt="Stars">&lt;/a>
&lt;a href="[lien suspect supprimé]">&lt;img src="[lien suspect supprimé]" alt="License">&lt;/a>
&lt;/p>

🌟 Introduction
DeepSeek RAG Chatbot is a powerful and intuitive application that allows you to have conversations with your own documents. By leveraging the speed of the Groq LPU Inference Engine and the versatility of LangChain, this tool transforms your static files (PDFs, DOCX, TXT, CSV) into an interactive knowledge base.

Simply upload your documents, and the system will automatically process, index, and prepare them for your questions. The user-friendly interface, built with Streamlit, makes it easy for anyone to get instant, accurate answers drawn directly from the provided content.

✨ Key Features
Multi-Format Document Support: Upload and process various file types, including .pdf, .docx, .txt, and .csv.
High-Speed Inferencing: Powered by Groq, delivering responses at exceptional speed for a fluid, real-time conversational experience.
Advanced RAG Pipeline: Utilizes LangChain for robust Retrieval-Augmented Generation, ensuring answers are relevant and contextually accurate.
Efficient Vector Storage: Employs ChromaDB to create and manage a persistent vector database of your document embeddings for fast retrieval.
User-Friendly Interface: A clean and simple web UI built with Streamlit that includes real-time processing feedback and chat history.
Open Source & Customizable: Fully open-source, allowing for easy customization and integration into other projects.
⚙️ How It Works
The application follows a sophisticated Retrieval-Augmented Generation (RAG) architecture to provide answers from your documents.

&lt;p align="center">
&lt;img src="[lien suspect supprimé]" alt="RAG Architecture Diagram" width="700">
&lt;/p>

Document Loading: You upload your documents (PDF, DOCX, etc.) through the Streamlit interface.
Text Splitting & Embedding: The system loads the documents, splits them into smaller, manageable chunks using LangChain, and generates vector embeddings for each chunk using HuggingFaceEmbeddings.
Vector Indexing: These embeddings are stored in a ChromaDB vectorstore, creating a searchable index of your document's knowledge.
User Query: You ask a question in the chat interface.
Context Retrieval: The system takes your query, embeds it, and performs a similarity search in ChromaDB to retrieve the most relevant document chunks (the "context").
Response Generation: The retrieved context and your original query are passed to the Groq-powered language model (like Llama3), which generates a human-like, accurate answer based on the provided information.
🚀 Getting Started
Follow these steps to set up and run the project on your local machine.

Prerequisites
Python 3.8+
A Groq API Key. You can get one for free at GroqCloud.
1. Clone the Repository
Bash

git clone https://github.com/samaraxmmar/Deepseek_chat_rag.git
cd Deepseek_chat_rag
2. Create a Virtual Environment
It's highly recommended to use a virtual environment to manage dependencies.

Bash

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
venv\Scripts\activate
3. Install Dependencies
Install all the required Python libraries using the requirements.txt file.

Bash

pip install -r requirements.txt
4. Set Up Your API Key
Create a file named .env in the root of the project folder and add your Groq API key:

GROQ_API_KEY="your_groq_api_key_here"
5. Run the Application
Launch the Streamlit application with the following command:

Bash

streamlit run streamlit_chat.py
Your web browser should automatically open to the application's interface.

📖 Usage
Launch the app: Run the streamlit run streamlit_chat.py command.
Upload Documents: Use the sidebar to upload one or more documents.
Wait for Processing: The sidebar will show a "Processing..." status while your documents are being loaded, chunked, embedded, and indexed. It will display "Documents Processed" when ready.
Ask Questions: Type your questions into the chat input at the bottom of the page and press Enter. The chatbot will provide answers based on the content of your uploaded documents.
Application Preview
&lt;p align="center">
&lt;img src="[lien suspect supprimé]" alt="Application Screenshot">
&lt;em>The main chat interface after processing documents.&lt;/em>
&lt;/p>

🤝 Contributing
Contributions are welcome! If you have suggestions for improvements or want to fix a bug, please feel free to:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature-name).
Make your changes and commit them (git commit -m 'Add some feature').
Push to the branch (git push origin feature/your-feature-name).
Open a Pull Request.
Please give this repository a ⭐ if you find it helpful!
