
# ⚡ Electrical Symbol Detection API

This project provides a FastAPI-based service for detecting electrical symbols — such as **EVSE**, **panelboards**, and **GFI outlets** — in construction blueprint **images** or **PDFs**, using a custom-trained **YOLOv8** model.

---

## 🚀 Features

- 🧠 **YOLOv8** object detection (custom-trained)
- 🖼️ Supports **images** (`.png`, `.jpg`, `.jpeg`, etc.)
- 📄 Supports **PDFs** (converts each page to an image)
- 📦 Returns detection results in JSON format
- 🖍️ Optional visual overlay for detections

---

## 🗂️ Project Structure

```
.
├── app.py                # FastAPI backend (with /detect endpoint)
├── runs/                 # YOLO training outputs
│   └── detect/train/weights/best.pt
├── data.yaml             # YOLO dataset configuration
├── requirements.txt
└── README.md
```

---

## 🛠️ Setup

### 1. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, install manually:

```bash
pip install fastapi uvicorn pillow pymupdf ultralytics
```

---

## 🏃 Run the API Server

```bash
uvicorn app:app --reload
```

---

## 🧪 Example Usage

### 💡 Detect symbols in an image

```bash
curl -X POST http://127.0.0.1:8000/detect \
  -F "file=@/path/to/image.png"
```

### 📄 Detect symbols in a PDF

```bash
curl -X POST http://127.0.0.1:8000/detect \
  -F "file=@/path/to/blueprint.pdf"
```

---

## 📤 API Response Format

```json
{
  "results": [
    {
      "page": 1,
      "detections": [
        {
          "class": "EVSE",
          "confidence": 0.91,
          "box": [x1, y1, x2, y2]
        }
      ]
    }
  ]
}
```

---

## 🧠 Model Training

This project uses a custom YOLOv8 model trained on blueprint images.

Train command:

```bash
yolo task=detect mode=train model=yolov8n.pt data=data.yaml epochs=50 imgsz=640
```

---

## 🛑 Notes

- PDF handling uses `PyMuPDF` to convert pages to images.
- The `/detect` endpoint supports both **single images** and **multi-page PDFs**.
- Outputs can be extended to return overlay images if needed.

---

## 📬 Contact

Developed by **Anubhav Anand**  
📧 anubhav.anand@example.com (replace with your email)

---
