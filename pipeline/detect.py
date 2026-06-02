from ultralytics import YOLO
import cv2
import requests
from datetime import datetime
import uuid

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)  

visitor_ids = set()
visitor_count = 0

while True:

    success, frame = cap.read()

    if not success:
        break

    results = model(frame)

    detections = results[0].boxes

    for box in detections:

        cls = int(box.cls[0])

        if cls == 0:

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            person_id = f"P_{x1//50}_{y1//50}"

            if person_id not in visitor_ids:

                visitor_ids.add(person_id)

                visitor_count += 1

                event = [
                    {
                        "event_id": str(uuid.uuid4()),
                        "store_id": "STORE_101",
                        "camera_id": "CAM_01",
                        "visitor_id": f"VIS_{visitor_count}",
                        "event_type": "ENTRY",
                        "timestamp": datetime.utcnow().isoformat(),
                        "zone_id": "BILLING",
                        "dwell_ms": 1000,
                        "is_staff": False,
                        "confidence": 0.95,
                        "metadata": {
                            "source": "YOLOv8"
                        }
                    }
                ]

                try:

                    requests.post(
                        "http://127.0.0.1:8000/events/ingest",
                        json=event
                    )

                except:

                    pass

    annotated_frame = results[0].plot()

    cv2.imshow(
        "Store Intelligence Detection",
        annotated_frame
    )

    if cv2.waitKey(1) & 0xFF == ord('q'):

        break

cap.release()
cv2.destroyAllWindows()
