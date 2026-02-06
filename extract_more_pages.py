import fitz  # PyMuPDF
import os

pdf_path = "shekhawati-mission-100-samajik-vigyan-10th-2026.pdf"
output_folder = "pdf_images"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

doc = fitz.open(pdf_path)

# Extract pages 9 to 15 (index 8 to 14)
# We already have page 8 (index 7).
# Let's extract a few more just to be safe, say up to page 20 to cover Chapter 2 and maybe start of 3.
start_page = 8  # Page 9
end_page = 20   # Page 21

for i in range(start_page, end_page):
    page = doc.load_page(i)
    pix = page.get_pixmap()
    output_path = f"{output_folder}/page_{i+1}.png"
    pix.save(output_path)
    print(f"Saved {output_path}")

doc.close()
