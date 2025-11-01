from pydantic import BaseModel

class DocumentScore(BaseModel):
    document: str
    score: float

class SearchResponse(BaseModel):
    results: list[DocumentScore]

class IngestResponse(BaseModel):
    message: str = "File ingested successfully"