from fastapi import UploadFile, File, HTTPException, APIRouter, BackgroundTasks
from collections import Counter

from libs import (
    search_top_k, 
    ingest_new_document, 
    tokenize, 
    check_if_document_exists, 
    SearchResponse, 
    IngestResponse, 
    DocumentScore, 
    logger
)
from constants import CHUNK_SIZE, MAX_FILE_SIZE

router = APIRouter()


@router.get("/")
def read_root():
    return {"message": "Hello, World!"}


@router.get("/search")
def search(query: str) -> SearchResponse:

    try:
        term = query.strip().lower()
        results = search_top_k(term, 3)
        return SearchResponse(results=[DocumentScore(document=doc, score=score) for doc, score in results])
    
    except HTTPException as e:
        logger.error(f"HTTPException: {e}")
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        logger.error(f"Exception: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.post("/ingest")
async def ingest(file: UploadFile, background_tasks: BackgroundTasks) -> IngestResponse:

    if not file.filename.endswith(".txt"):
        raise HTTPException(status_code=400, detail="File must be a .txt file")

    if file.size > MAX_FILE_SIZE:
        raise HTTPException(status_code=413, detail="File size exceeds the maximum allowed size")

    if check_if_document_exists(file.filename):
        raise HTTPException(status_code=400, detail="Document already exists")
        

    term_freq = Counter()

    try:
        while chunk := await file.read(CHUNK_SIZE):          

            text = chunk.decode("utf-8")
            tokens = tokenize(text)
            term_freq.update(tokens)

        logger.info(f"Tokenized {len(term_freq)} tokens from {file.filename}")
        logger.info("Pushing background task to ingest document")

        background_tasks.add_task(ingest_new_document, file.filename, term_freq)

        return IngestResponse(message="File ingested successfully")
    
    except HTTPException as e:
        logger.error(f"HTTPException: {e}")
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        logger.error(f"Exception: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
