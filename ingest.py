from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

from dotenv import load_dotenv
import os

load_dotenv()  # 读取 .env 文件，确保环境变量加载
print("OpenAI API Key:", os.getenv("OPENAI_API_KEY"))  # 打印检查一下

DATA_DIR = Path("data/pdf/embedded")
VECTORDB_DIR = Path("vector_db")

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

def embed_documents(chunks):
    embeddings = OpenAIEmbeddings()
    vectordb = FAISS.from_documents(chunks, embeddings)
    vectordb.save_local(str(VECTORDB_DIR))
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