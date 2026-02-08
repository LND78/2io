import fitz
import os

pdf_path = "shekhawati-mission-100-samajik-vigyan-10th-2026.pdf"
output_dir = "pages"
os.makedirs(output_dir, exist_ok=True)

try:
    doc = fitz.open(pdf_path)
    # Pages 31 to 50 correspond to indices 30 to 49
    start_page = 30
    end_page = 49

    for i in range(start_page, end_page + 1):
        page = doc.load_page(i)
        pix = page.get_pixmap()
        image_path = os.path.join(output_dir, f"page_{i+1}.png")
        pix.save(image_path)
        print(f"Saved {image_path}")

except Exception as e:
    print(f"Error: {e}")
