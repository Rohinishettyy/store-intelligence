from fastapi import APIRouter
from typing import List
from app.models import Event

router = APIRouter()

events_db = [
    {
        "event_id": "1",
        "store_id": "STORE_101",
        "camera_id": "CAM_1",
        "visitor_id": "V1",
        "event_type": "ENTRY",
        "timestamp": "2026-06-01",
        "zone_id": "BILLING",
        "dwell_ms": 1000,
        "is_staff": False,
        "confidence": 0.9,
        "metadata": {}
    }
]


@router.post("/events/ingest")
def ingest_events(events: List[Event]):
    for event in events:
        events_db.append(event.dict())

    return {
        "message": "Events ingested successfully",
        "total_events": len(events)
    }