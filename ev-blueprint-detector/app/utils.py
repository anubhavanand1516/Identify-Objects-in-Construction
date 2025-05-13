from pdf2image import convert_from_bytes
from PIL import Image
import cv2
import numpy as np
import os

def convert_pdf_to_image(pdf_bytes):
    images = convert_from_bytes(pdf_bytes, dpi=150)
    return images[0]  # First page only

def draw_boxes(image, detections):
    for det in detections:
        x, y, w, h = map(int, det['bbox'])
        label = det['label']
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(image, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (36,255,12), 2)
    return image
