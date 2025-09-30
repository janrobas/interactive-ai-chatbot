import streamlit as st
from config import Config
from rag import RAG

rag = RAG(qdrant_url=Config.QDRANT_URL, embedding_model=Config.EMBEDDING_MODEL, llama_model = Config.LLAMA_MODEL)
chain = rag.get_chain(collection_name=Config.COLLECTION_NAME)

st.title("Interactive Chatbot")
st.write("Ask any question, and the chatbot will respond using context from the vector database!")

user_query = st.text_input("Enter your question here:", value="Who teaches AI course?")

if st.button("Get Response"):
    with st.spinner("Generating response..."):
        try:
            response = chain.invoke({"input": user_query})
            st.success("Response:")
            st.write(response["answer"])
        except Exception as e:
            st.error(f"An error occurred: {e}")