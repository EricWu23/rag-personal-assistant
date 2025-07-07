from fastapi import APIRouter,Request
from app.schemas import QueryRequest, QueryResponse, SourceDocument
from rag_assistant.rag_chain import get_qa_chain
from fastapi.responses import JSONResponse


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

@router.post("/bot")
async def bot_webhook(request: Request):
   body = await request.json()
   user_input = body.get("text", "")
   
   # 调用现有 RAG 服务
   result = qa_chain.invoke({"query": user_input})
   answer = result["result"]
   
   # 返回符合 Bot Framework 的消息
   return JSONResponse(content={
        "type": "message",
        "text": answer
        })
