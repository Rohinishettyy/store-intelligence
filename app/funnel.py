from fastapi import APIRouter
from app.ingestion import events_db

router = APIRouter()


@router.get("/stores/{store_id}/funnel")
def get_funnel(store_id: str):

    store_events = [
        e for e in events_db
        if e["store_id"] == store_id
    ]

    entries = len([
        e for e in store_events
        if e["event_type"] == "ENTRY"
    ])

    billing = len([
        e for e in store_events
        if e.get("zone_id") == "BILLING"
    ])

    return {
        "store_id": store_id,
        "funnel": {
            "entries": entries,
            "billing_visits": billing
        }
    }