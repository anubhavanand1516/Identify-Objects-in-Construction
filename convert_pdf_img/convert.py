from pdf2image import convert_from_path
from pathlib import Path

# Set up output directory
output_dir = Path("/mnt/data/dataset/images")
output_dir.mkdir(parents=True, exist_ok=True)

# Convert PDF pages to high-resolution PNGs
pdf_path = "/mnt/data/The Egyptian EV - Sample Data.pdf"
images = convert_from_path(pdf_path, dpi=200)

# Save first two pages as E003.png and E004.png
output_paths = []
for i, name in enumerate(["E003", "E004"]):
    image_path = output_dir / f"{name}.png"
    images[i].save(image_path, "PNG")
    output_paths.append(str(image_path))

output_paths
