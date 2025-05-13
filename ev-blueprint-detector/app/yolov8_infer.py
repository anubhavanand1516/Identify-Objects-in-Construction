from ultralytics import YOLO
import numpy as np

model = YOLO("yolov8/best.pt")
CLASS_NAMES = ['evse', 'panel', 'gfi']

def predict(image: np.ndarray):
    results = model(image)[0]
    detections = []

    for box in results.boxes:
        conf = float(box.conf[0])
        if conf < 0.3:
            continue
        cls = int(box.cls[0])
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        detections.append({
            "label": CLASS_NAMES[cls],
            "confidence": round(conf, 2),
            "bbox": [x1, y1, x2 - x1, y2 - y1]
        })

    return detections
