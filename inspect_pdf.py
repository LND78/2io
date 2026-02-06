import fitz  # PyMuPDF
import os

pdf_path = "shekhawati-mission-100-samajik-vigyan-10th-2026.pdf"
output_folder = "pdf_images"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

try:
    doc = fitz.open(pdf_path)
    # Convert first 3 pages
    for i in range(min(3, len(doc))):
        page = doc.load_page(i)  # number of page
        pix = page.get_pixmap()
        image_path = os.path.join(output_folder, f"page_{i+1}.png")
        pix.save(image_path)
        print(f"Saved {image_path}")
    doc.close()
except Exception as e:
    print(f"Error: {e}")
