from rag_assistant.rag_chain import get_qa_chain

qa_chain = get_qa_chain()

def ask_cli():
    while True:
        q = input("❓ Your question (or 'exit'): ")
        if q.lower() == "exit":
            break
        result = qa_chain.invoke({"query": q})
        print("\n🧠 Answer:\n", result["result"])
        print("\n📚 Source documents:")
        for i, doc in enumerate(result["source_documents"], 1):
            print(f"--- Source {i} ---")
            print("Path:", doc.metadata.get('source_path'))
            print("Excerpt:", doc.page_content[:300], "...\n")

if __name__ == "__main__":
    ask_cli()