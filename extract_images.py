from pypdf import PdfReader
from PIL import Image
import io

reader = PdfReader("shekhawati-mission-100-samajik-vigyan-10th-2026.pdf")

# Try page 50 (51st page)
page = reader.pages[50]

count = 0
for image_file_object in page.images:
    with open(f"page_51_image_{count}.png", "wb") as fp:
        fp.write(image_file_object.data)
    count += 1

print(f"Extracted {count} images from page 51")
