import cv2
import os

# Config
img_path = "/Users/anubhavanand/Desktop/images/E003.png"
label_path = "/Users/anubhavanand/Desktop/labels/E003.txt"
output_path = "/Users/anubhavanand/Desktop/hello/E003_annotated.png"
class_names = ["evse", "panel", "gfi"]

# Assign different colors for each class (BGR format)
colors = {
    0: (0, 0, 255),     # Red for EVSE
    1: (0, 255, 0),     # Green for Panel
    2: (255, 0, 0)      # Blue for GFI
}

# Load image
img = cv2.imread(img_path)
if img is None:
    print("❌ Failed to load image.")
    exit()
h, w, _ = img.shape

# Draw boxes
with open(label_path, "r") as f:
    for line in f:
        if line.strip() == "":
            continue
        class_id, x_center, y_center, box_w, box_h = map(float, line.strip().split())
        class_id = int(class_id)

        # Convert YOLO to top-left and bottom-right corner
        x1 = int((x_center - box_w / 2) * w)
        y1 = int((y_center - box_h / 2) * h)
        x2 = int((x_center + box_w / 2) * w)
        y2 = int((y_center + box_h / 2) * h)

        color = colors.get(class_id, (255, 255, 255))  # Default white if unknown
        label = class_names[class_id]

        # Draw rectangle and label
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
        cv2.putText(img, label, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

# Save result
os.makedirs(os.path.dirname(output_path), exist_ok=True)
cv2.imwrite(output_path, img)
print(f"✅ Annotated image saved: {output_path}")
