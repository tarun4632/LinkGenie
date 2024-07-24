import os
import streamlit as st

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders.url import UnstructuredURLLoader
from langchain_community.vectorstores import FAISS
from langchain.chains.qa_with_sources.retrieval import RetrievalQAWithSourcesChain

from dotenv import load_dotenv
load_dotenv()
# Page configuration
st.set_page_config(page_title="LinkGenie", page_icon="🧞", layout="wide")

# Custom CSS for dark theme
st.markdown("""
    <style>
    .main > div {
        padding-top: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
    }
    .stTextInput>div>div>input {
        background-color: #2b313e;
        color: #ffffff;
    }
    .stAlert {
        background-color: #1e2530;
        color: #ffffff;
    }
    .stSuccess {
        background-color: #145214;
        color: #ffffff;
    }
    .stInfo {
        background-color: #1c3f5f;
        color: #ffffff;
    }
    </style>
    """, unsafe_allow_html=True)

# Main title with emoji
st.title("🧞 LinkGenie")

# Sidebar
with st.sidebar:
    st.header("📚 URL Input")
    urls = []
    for i in range(3):
        url = st.text_input(f"URL {i+1}", key=f"url_{i}")
        if url:
            urls.append(url)

    process_url_clicked = st.button("🔍 Process URLs", type="primary")

# Main content area
main_placeholder = st.empty()

# Initialize session state
if 'processed' not in st.session_state:
    st.session_state.processed = False

# File path for FAISS index
file_path = "faiss_index"

# Load the model
llm = ChatOpenAI(model="gpt-3.5-turbo")

# Process URLs
if process_url_clicked and urls:
    with st.spinner("Processing URLs..."):
        # Load the data from the URLs
        loader = UnstructuredURLLoader(urls=urls)
        data = loader.load()

        # Split the data into chunks
        splitter = RecursiveCharacterTextSplitter(
            separators=['\n\n', '\n', '.', '?'],
            chunk_size=1000,
            chunk_overlap=100
        )
        docs = splitter.split_documents(data)

        # Create and Load the embeddings
        embeddings = OpenAIEmbeddings()
        vectorstore_openapi = FAISS.from_documents(docs, embeddings)

        # Save the vectorstore
        vectorstore_openapi.save_local(file_path)

        st.session_state.processed = True
        st.success("URLs processed successfully!")

# Query input and processing
if st.session_state.processed:
    query = st.text_input("🔎 Ask a question about the content:", key="query")
    if query:
        if os.path.exists(file_path):
            with st.spinner("Searching for answers..."):
                embeddings = OpenAIEmbeddings()
                vectorstore_openapi = FAISS.load_local(file_path, embeddings, allow_dangerous_deserialization=True)
                chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorstore_openapi.as_retriever(),
                                                             verbose = False)
                result = chain.invoke({"question": query}, return_only_outputs=True)

                st.subheader("📝 Answer")
                st.markdown(f"<div style='background-color: #2b313e; padding: 1rem; border-radius: 0.5rem;'>{result['answer']}</div>", unsafe_allow_html=True)

                st.subheader("🔗 Sources")
                st.info(result['sources'])
else:
    with main_placeholder.container():
        st.info("👈 Please enter URLs in the sidebar and click 'Process URLs' to get started.")

# Footer
st.markdown("---")
st.markdown("<div style='text-align: center; color: #4CAF50;'>Built with ❤️ using Streamlit and LangChain</div>", unsafe_allow_html=True)