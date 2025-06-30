from pathlib import Path
import pickle
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

from dotenv import load_dotenv
import os

load_dotenv()  # 读取 .env 文件，确保环境变量加载
print("OpenAI API Key:", os.getenv("OPENAI_API_KEY"))  # 打印检查一下

DATA_DIR = Path("data/pdf/embedded")
CHUNKS_PATH = Path("intermediate/chunks.pkl")
VECTORDB_DIR = Path("vector_db")

def save_chunks(chunks, path=CHUNKS_PATH):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "wb") as f:
        pickle.dump(chunks, f)

def load_chunks(path=CHUNKS_PATH):
    with open(path, "rb") as f:
        return pickle.load(f)

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

# 可选模型："openai"（默认）或 "local"
def embed_documents(chunks, model_type="local"):
    print(f"📦 Embedding {len(chunks)} chunks...")

    if model_type == "local":
        from langchain_huggingface import HuggingFaceEmbeddings
        print("💻 Using HuggingFace local embeddings (all-MiniLM-L6-v2)...")
        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    else:
        from langchain_openai import OpenAIEmbeddings
        print("🌐 Using OpenAI embeddings...")
        embeddings = OpenAIEmbeddings()

    vectordb = FAISS.from_documents(chunks, embeddings)

    print(f"🧠 FAISS index size: {vectordb.index.ntotal}")  # 👈 新增打印

    VECTORDB_DIR.mkdir(exist_ok=True, parents=True)
    vectordb.save_local(str(VECTORDB_DIR))
    print(f"✅ Vector DB saved to: {VECTORDB_DIR}")
    return vectordb

def main(mode="full", model_type = "local"):
    if mode == "full":
        print("🚀 [FULL] Running full pipeline: load → chunk → embed")
        print("🚀 Starting ingestion pipeline...")
        docs = load_documents(DATA_DIR)
        print(f"📄 Loaded {len(docs)} documents")
        chunks = chunk_documents(docs)
        save_chunks(chunks)
    elif mode == "embed_only":
        print("🚀 [DEBUG] Loading chunks from disk...")
        chunks = load_chunks()
    else:
        raise ValueError(f"Unknown mode: {mode}")
    
    print(f"✂️  Split into {len(chunks)} chunks")
    vectordb=embed_documents(chunks,model_type="local")
    print("🚀 Ingestion completed!")

if __name__ == "__main__":
    main(mode="embed_only", model_type="local")