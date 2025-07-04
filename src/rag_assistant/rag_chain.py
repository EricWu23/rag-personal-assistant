from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from rag_assistant.retrieve import load_vectorstore
from rag_assistant.config import *
from rag_assistant.llm_router import get_llm


def get_qa_chain():
    vectordb = load_vectorstore()
    retriever = vectordb.as_retriever(search_type="mmr", search_kwargs={"k": 10})

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""

You are an expert technical assistant. 
Use the provided context to answer the question. 
Be specific. 
If the answer is suggested or hinted at, you may infer it.

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