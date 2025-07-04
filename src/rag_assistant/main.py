from pathlib import Path
from rag_assistant.retrieve import search
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

def main():
    index_path = Path("faiss_index.pkl")
    llm = ChatOpenAI(model="gpt-3.5-turbo")
    print("输入问题(q退出)：")
    while True:
        query = input(">> ")
        if query.lower() in ("q", "quit", "exit"):
            break
        docs = search(query, index_path)
        context = "\n\n".join(d.page_content for d in docs)
        prompt = [
            SystemMessage(content="你是一个知识问答助手，基于以下内容回答问题：\n" + context),
            HumanMessage(content=query),
        ]
        resp = llm(prompt)
        print("🦜️ 回答：", resp.content)

if __name__ == "__main__":
    main()