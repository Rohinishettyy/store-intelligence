from fastapi import APIRouter
from app.ingestion import events_db

router = APIRouter()


@router.get("/stores/{store_id}/heatmap")
def get_heatmap(store_id: str):

    store_events = [
        event for event in events_db
        if event["store_id"] == store_id
    ]

    zone_counts = {}

    for event in store_events:

        zone = event.get("zone_id", "UNKNOWN")

        if zone not in zone_counts:

            zone_counts[zone] = 0

        zone_counts[zone] += 1

    return {
        "store_id": store_id,
        "heatmap": zone_counts
    }
