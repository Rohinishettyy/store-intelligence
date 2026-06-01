from fastapi import APIRouter
from app.ingestion import events_db

router = APIRouter()


@router.get("/stores/{store_id}/anomalies")
def detect_anomalies(store_id: str):

    store_events = [
        event for event in events_db
        if event["store_id"] == store_id
    ]

    anomalies = []

    if len(store_events) > 50:
        anomalies.append(
            "High visitor spike detected"
        )

    billing_events = [
        event for event in store_events
        if event.get("zone_id") == "BILLING"
    ]

    if len(billing_events) > 20:
        anomalies.append(
            "Billing queue congestion detected"
        )

    if len(anomalies) == 0:
        anomalies.append(
            "No anomalies detected"
        )

    return {
        "store_id": store_id,
        "anomalies": anomalies
    }