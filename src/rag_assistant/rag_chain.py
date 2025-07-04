from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from rag_assistant.retrieve import load_vectorstore
from rag_assistant.config import *
from rag_assistant.llm_router import get_llm


def get_qa_chain():
    vectordb = load_vectorstore()
    retriever = vectordb.as_retriever(search_kwargs={"k": 3})

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""
你是一位专业的助手，请根据以下文档内容回答问题。
<context>
{context}
</context>

问题：{question}
回答：
"""
    )

    llm = get_llm()
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt},
        return_source_documents=True,
        verbose=VERBOSE_MODE
    )
    return qa_chain