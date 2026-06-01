from fastapi import APIRouter
from app.ingestion import events_db

router = APIRouter()


@router.get("/stores/{store_id}/metrics")
def get_metrics(store_id: str):

    store_events = [
        event for event in events_db
        if event["store_id"] == store_id
    ]

    unique_visitors = len(
        set(event["visitor_id"] for event in store_events)
    )

    total_entries = len(
        [e for e in store_events if e["event_type"] == "ENTRY"]
    )

    total_exits = len(
        [e for e in store_events if e["event_type"] == "EXIT"]
    )

    return {
        "store_id": store_id,
        "unique_visitors": unique_visitors,
        "entries": total_entries,
        "exits": total_exits,
        "total_events": len(store_events)
    }