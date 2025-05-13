from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import shutil
import os
import cv2
import numpy as np
from PIL import Image
from app.utils import convert_pdf_to_image, draw_boxes
from app.yolov8_infer import predict

app = FastAPI()

@app.post("/detect")
async def detect(file: UploadFile = File(...)):
    ext = file.filename.split(".")[-1].lower()
    contents = await file.read()

    if ext == "pdf":
        image_pil = convert_pdf_to_image(contents)
    else:
        image_pil = Image.open(file.file).convert("RGB")

    image_np = np.array(image_pil)
    detections = predict(image_np.copy())
    overlayed = draw_boxes(image_np.copy(), detections)

    os.makedirs("static", exist_ok=True)
    overlay_path = "static/overlay.png"
    cv2.imwrite(overlay_path, overlayed[:, :, ::-1])  # RGB to BGR

    return JSONResponse({
        "detections": detections,
        "image_url": "https://<your-space>.hf.space/file/overlay.png"
    })
