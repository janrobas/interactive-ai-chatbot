# RAG System with Qdrant and Ollama

A Retrieval-Augmented Generation (RAG) system that combines vector search with large language models to provide context-aware answers.

I have used this as a reference:
https://medium.com/@spandanmaity58/implementing-rag-using-langchain-ollama-and-qdrant-8b7b832fc3da

Parts of this have been vibe-coded with DeepSeek.

## 🚀 Features

- **Document Ingestion**: Add and chunk documents into a vector database
- **Semantic Search**: Find relevant context using vector similarity
- **LLM Integration**: Generate answers using Ollama with LLaMA models
- **Web Interface**: User-friendly Streamlit chatbot interface
- **Modular Design**: Easy to configure and extend

## 🛠️ Architecture
```
Text Documents → Chunking → Embedding → Qdrant Vector Store
↓
User Query → Vector Search → Context + Query → Ollama LLM → Answer
```

## 📋 Prerequisites

- Python 3.8+
- [Ollama](https://ollama.ai/) installed and running
- [Qdrant](https://qdrant.tech/) vector database
- Required Python packages

## ⚙️ Installation

1. **Clone the repository**
```
bash
git clone <your-repo-url>
cd interactive-ai-chatbot
```

2. **Create virtual environment**
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```
pip install -r requirements.txt
```

4. **Set up environment variables**
```
cp .env.example .env
# Edit .env with your configuration
```

5. **Start services**

Start Qdrant (using Docker)
```
docker run -p 6333:6333 qdrant/qdrant
```

Start Ollama and pull model
```
ollama pull llama3.2:1b 
```

## 🎯 Usage

1. **Test Ingestion and Queries**
```
python test_ingestion.py
```

2. **Launch Web Interface**
```
streamlit run app.py
```

3. **Add Your Documents**
Modify `test_ingestion.py` to include your own documents:

```
texts = [
    "Your document text here...",
    "Another document...",
]
```