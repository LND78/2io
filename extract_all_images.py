from pypdf import PdfReader
from PIL import Image
import io
import os

reader = PdfReader("shekhawati-mission-100-samajik-vigyan-10th-2026.pdf")

# Indices 50 to 64 (inclusive) corresponds to pages 51 to 65
for i in range(50, 65):
    try:
        page = reader.pages[i]
        count = 0
        for image_file_object in page.images:
            # We assume the main page content is the largest image or the first one.
            # Usually these scanned PDFs are one large image per page.
            with open(f"page_{i+1}.png", "wb") as fp:
                fp.write(image_file_object.data)
            count += 1
        print(f"Extracted {count} images from page {i+1}")
    except Exception as e:
        print(f"Error extracting page {i+1}: {e}")
