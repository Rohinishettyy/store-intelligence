from fastapi import APIRouter
from app.ingestion import events_db

router = APIRouter()


@router.get("/health")
def health():

    return {
        "status": "healthy",
        "total_events": len(events_db)
    }