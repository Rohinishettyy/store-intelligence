from fastapi import APIRouter
from app.ingestion import events_db

router = APIRouter()


@router.get("/stores/{store_id}/queue")
def get_queue_status(store_id: str):

    store_events = [
        event for event in events_db
        if event["store_id"] == store_id
    ]

    billing_events = [
        event for event in store_events
        if event.get("zone_id") == "BILLING"
    ]

    queue_count = len(billing_events)

    status = "NORMAL"

    if queue_count > 10:
        status = "HIGH"

    if queue_count > 20:
        status = "CRITICAL"

    return {
        "store_id": store_id,
        "queue_count": queue_count,
        "queue_status": status
    }