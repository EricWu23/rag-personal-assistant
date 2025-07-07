from pydantic import BaseModel
from typing import List, Optional

class QueryRequest(BaseModel):
    query: str

class SourceDocument(BaseModel):
    path: str
    excerpt: str

class QueryResponse(BaseModel):
    answer: str
    sources: Optional[List[SourceDocument]] = []