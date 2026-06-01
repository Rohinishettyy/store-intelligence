from fastapi import FastAPI

from app.ingestion import router as ingestion_router
from app.metrics import router as metrics_router
from app.heatmap import router as heatmap_router
from app.anomaly import router as anomaly_router
from app.queue import router as queue_router

app = FastAPI(
    title="Store Intelligence Dashboard API"
)

app.include_router(ingestion_router)

app.include_router(metrics_router)

app.include_router(heatmap_router)

app.include_router(anomaly_router)

app.include_router(queue_router)


@app.get("/")
def home():

    return {
        "message": "Store Intelligence Dashboard API Running"
    }