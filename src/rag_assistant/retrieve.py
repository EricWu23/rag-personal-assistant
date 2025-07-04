from pathlib import Path
from langchain_community.vectorstores import FAISS
from rag_assistant.config import VECTORDB_DIR, EMBEDDING_MODEL_TYPE, EMBEDDING_MODEL_NAME

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

def load_vectorstore():
    embeddings = get_embedding_model()
    vectordb = FAISS.load_local(str(VECTORDB_DIR),
                                embeddings,
                                allow_dangerous_deserialization=True)
    return vectordb

def search(query: str, top_k=3):
    vectordb = load_vectorstore()
    docs = vectordb.similarity_search(query, k=top_k)
    return docs

if __name__ == "__main__":
    query = input("请输入查询内容: ")
    results = search(query)
    print(f"🔍 查询: {query}")
    for i, doc in enumerate(results, 1):
        print(f"\n--- 📄 结果 {i} ---")
        print(doc.page_content.strip()[:300] + "...")
        print(f"📂 来源: {doc.metadata.get('source_path', '未知')}")
