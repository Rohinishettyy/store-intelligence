from fastapi import APIRouter
from typing import List
from app.models import Event

router = APIRouter()

events_db = []


@router.post("/events/ingest")
def ingest_events(events: List[Event]):
    for event in events:
        events_db.append(event.dict())

    return {
        "message": "Events ingested successfully",
        "total_events": len(events)
    }