import streamlit as st
from config import Config
from rag import RAG

# Initialize RAG system
@st.cache_resource
def initialize_rag():
    return RAG(
        qdrant_url=Config.QDRANT_URL,
        embedding_model=Config.EMBEDDING_MODEL,
        llama_model=Config.LLAMA_MODEL
    )

def main():
    st.set_page_config(
        page_title="RAG Chatbot",
        page_icon="🤖",
        layout="centered"
    )
    
    st.title("🧠 RAG-Powered Chatbot")
    st.markdown("Ask questions and get answers based on the documents in our knowledge base!")
    
    # Initialize RAG
    rag = initialize_rag()
    
    # Create chain (cached to avoid recreation on every interaction)
    @st.cache_resource
    def get_chain():
        return rag.get_chain(collection_name=Config.COLLECTION_NAME)
    
    chain = get_chain()
    
    # Sidebar for information
    with st.sidebar:
        st.header("ℹ️ About")
        st.markdown("""
        This chatbot uses:
        - **RAG** (Retrieval-Augmented Generation)
        - **Qdrant** vector database
        - **Ollama** with LLaMA model
        - **Sentence Transformers** for embeddings
        """)
        
        st.header("⚙️ Configuration")
        st.text(f"Model: {Config.LLAMA_MODEL}")
        st.text(f"Embeddings: {Config.EMBEDDING_MODEL}")
        st.text(f"Collection: {Config.COLLECTION_NAME}")
    
    # Main chat interface
    user_query = st.text_input(
        "💬 Ask your question:",
        placeholder="e.g., Who teaches the AI course?",
        key="user_input"
    )
    
    col1, col2 = st.columns([1, 5])
    with col1:
        ask_button = st.button("Ask", type="primary", use_container_width=True)
    with col2:
        clear_button = st.button("Clear", use_container_width=True)
    
    if clear_button:
        st.rerun()
    
    if ask_button and user_query:
        with st.spinner("🔍 Searching and generating answer..."):
            try:
                response = chain.invoke({"input": user_query})
                
                st.success("✅ Answer:")
                st.info(response["answer"])
                
            except Exception as e:
                st.error(f"❌ An error occurred: {str(e)}")
                st.info("Please make sure Qdrant and Ollama are running.")

if __name__ == "__main__":
    main()