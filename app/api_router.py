from fastapi import APIRouter
from app.schemas import QueryRequest, QueryResponse, SourceDocument
from rag_assistant.rag_chain import get_qa_chain

router = APIRouter()
qa_chain = get_qa_chain()

@router.post("/query", response_model=QueryResponse)
def ask_question(request: QueryRequest):
    result = qa_chain.invoke({"query": request.query})

    sources = [
        SourceDocument(
            path=doc.metadata.get("source_path", "Unknown"),
            excerpt=doc.page_content[:300]
        )
        for doc in result.get("source_documents", [])
    ]

    return QueryResponse(
        answer=result["result"],
        sources=sources
    )