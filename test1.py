from config import Config
from rag import RAG

rag = RAG(qdrant_url=Config.QDRANT_URL, embedding_model=Config.EMBEDDING_MODEL, llama_model = Config.LLAMA_MODEL)

# texts = [
#     {"text": 'Name of the professor for AI is Jan. He is also teaching several other courses, like intro to programming. His name is Jan Robas.', "metadata":{'source': 'wikipedia.com'}},
# ]
# ans = rag.dodaj(text_array=texts, collection_name=collection_name)
# texts = [
#     "Name of the professor for AI is Jan. He is also teaching several other courses, like intro to programming. His name is Jan Robas."
# ]
# ans = rag.dodaj(text_array=texts, collection_name=collection_name)

ques = "What is the name of the professor that teaches programming course?"
ans = rag.odgovori(question=ques, collection_name=Config.COLLECTION_NAME)
print(ans)