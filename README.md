
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


### 1. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

## 🛠️ convert_pdf_img
```
.
├── convert.py                          # convert PDF to image        
├── The Egyptian EV - Sample Data.pdf   # sample pdf
│   
```
```bash
python convert.py
```

## 🛠️ datasets

```
datasets/
├── data/
│   ├── yolov8n.pt
│   ├── data.yaml
│   ├── data/
│   │   ├── images/
│   │   │   ├── train/
│   │   │   │   ├── E003.png
│   │   │   ├── val/
│   │   │   │   ├── E004.png
│   │   ├── labels/
│   │   │   ├── train/
│   │   │   │   ├── E003.txt
│   │   │   ├── val/
│   │   │   │   ├── E004.txt
│   │   │   ├── train.cache
│   │   │   ├── val.cache
│   ├── runs/detect/train/weight/best.pt
 
```
```bash
pip install -r requirements.txt
```
```bash
yolo task=detect mode=train model=yolov8n.pt data=data.yaml epochs=50 imgsz=640
```
## 🛠️ test_annotation
```
.
├── annotation.py                # check if the annotation was correctly       
├── E003_annotated.png           #annotation image
│   
```
![E003_annotated](https://github.com/user-attachments/assets/67c5d4c3-7098-4dd7-8f89-72bf48ae70b5)


## 🏃 Run the API Server

```bash
uvicorn app.main:app --reload
```
<img width="773" alt="Screenshot 2025-05-13 at 7 14 52 PM" src="https://github.com/user-attachments/assets/aa781030-264c-4eee-8f18-1162ae53dff8" />

---

## 🧪 Example Usage

### 💡 Detect symbols in an image

```bash
anubhavanand@Anubhavs-MacBook-Air ~ % curl -X POST http://127.0.0.1:8000/detect \
  -F "file=@/Users/anubhavanand/Desktop/datasets/data/images/train/E003.png""
```
<img width="569" alt="Screenshot 2025-05-13 at 7 17 21 PM" src="https://github.com/user-attachments/assets/d07b6d13-0fc6-4ec2-8a99-b58618c76c98" />

---

## 📤 How to Deploy and Use

Follow these steps to deploy and run your app:

1.⁠ ⁠Go to [Hugging Face Spaces](https://huggingface.co/spaces)

2.⁠ ⁠Open your Space (click on its name)

3.⁠ ⁠Make sure the following files are uploaded:
   - ⁠ app.py ⁠
   - ⁠ yolov8_infer.py ⁠
   - ⁠ requirements.txt ⁠
   - ⁠ best.pt ⁠ (your trained model)

4.⁠ ⁠After uploading:
   - The app will automatically *build and launch*
   - In a few seconds, you'll see the app running inline

```
ev_symbol_detector_json_output/
├── app.py                 ← Main entry point for the Gradio app (JSON output format)
├── yolov8_infer.py        ← Loads YOLO model, runs detection, and returns structured JSON + saves overlay image
├── requirements.txt       ←Ensures ultralytics, gradio, Pillow are installed in the Hugging Face Space
├── outputs/               ← Runtime folder where annotated image files are stored and accessed via image_url
└── best.pt      ← Your trained YOLOv8 model — must be uploaded manually
```



5.⁠ ⁠Your *live public link* will appear in the browser’s URL bar: https://huggingface.co/spaces/Anubhav1516/Deploy


<img width="1440" alt="Screenshot 2025-05-13 at 7 47 54 PM" src="https://github.com/user-attachments/assets/27cac3ef-7ddc-4c19-8d3c-3e70f06ab560" />


