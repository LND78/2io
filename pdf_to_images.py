import fitz  # PyMuPDF
import sys
import os

pdf_path = "class-10-maths-shekhawati-mission-100-2026.pdf"
output_folder = "images"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

if not os.path.exists(pdf_path):
    print(f"Error: {pdf_path} not found")
    sys.exit(1)

doc = fitz.open(pdf_path)
print(f"Total pages: {len(doc)}")

# Convert all pages
for i in range(len(doc)):
    page = doc.load_page(i)  # number of page
    pix = page.get_pixmap()
    output = f"{output_folder}/page_{i+1}.png"
    pix.save(output)
    if (i+1) % 10 == 0:
        print(f"Saved {output}")
print("All pages saved.")
