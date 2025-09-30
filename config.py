import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Qdrant Configuration
    QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")
    COLLECTION_NAME = os.getenv("COLLECTION_NAME", "test_collection_1")
    
    # Model Configuration
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
    LLAMA_MODEL = os.getenv("LLAMA_MODEL", "llama3.2:1b")
