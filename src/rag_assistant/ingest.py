from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from rag_assistant.config import LLM_TYPE, LOCAL_MODEL_PATH,DATA_DIR, EMBEDDING_MODEL_TYPE, EMBEDDING_MODEL_NAME, VECTORDB_DIR

from dotenv import load_dotenv
import os

load_dotenv()  # 读取 .env 文件，确保环境变量加载
print("OpenAI API Key:", os.getenv("OPENAI_API_KEY"))  # 打印检查一下


def load_documents(data_dir: Path):
    documents = []
    for path in data_dir.rglob("*.pdf"):
        print(f"🔍 Loading: {path}")
        loader = PyPDFLoader(str(path))
        docs = loader.load()
        for doc in docs:
            doc.metadata["source_path"] = str(path)
            doc.metadata["source_type"] = "pdf"
        documents.extend(docs)
    return documents

def chunk_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        separators=["\n\n", "\n", ".", "!", "?", " ", ""]
    )
    return splitter.split_documents(documents)

def get_embedding_model():
    if EMBEDDING_MODEL_TYPE == "openai":
        from langchain_openai import OpenAIEmbeddings
        print("🔌 Using OpenAI Embeddings")
        return OpenAIEmbeddings()
    elif EMBEDDING_MODEL_TYPE == "huggingface":
        from langchain_huggingface import HuggingFaceEmbeddings
        print(f"💻 Using HuggingFace Embeddings: {EMBEDDING_MODEL_NAME}")
        return HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
    else:
        raise ValueError(f"❌ Unsupported embedding model type: {EMBEDDING_MODEL_TYPE}")
    
def embed_documents(chunks):
    print(f"📦 Embedding {len(chunks)} chunks...")
    embeddings = get_embedding_model()
    vectordb = FAISS.from_documents(chunks, embeddings)

    vector_path = Path(VECTORDB_DIR)
    vector_path.mkdir(parents=True, exist_ok=True)
    vectordb.save_local(str(vector_path))
    print(f"✅ Vector DB saved to: {VECTORDB_DIR}")
    return vectordb

def main():
    print("🚀 Starting ingestion pipeline...")
    docs = load_documents(DATA_DIR)
    print(f"📄 Loaded {len(docs)} documents")
    chunks = chunk_documents(docs)
    print(f"✂️  Split into {len(chunks)} chunks")
    embed_documents(chunks)
    print("🚀 Ingestion completed!")

if __name__ == "__main__":
    main()