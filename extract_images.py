from pypdf import PdfReader
import os

reader = PdfReader("shekhawati-mission-100-samajik-vigyan-10th-2026.pdf")
start_page = 30 # Page 31
end_page = 50   # Page 50 (exclusive in range means up to 49, so actually 50 pages means index 49)
# User said pages 31 to 50. Python uses 0-based index.
# So indices are 30 to 49 inclusive.

output_dir = "extracted_images"
os.makedirs(output_dir, exist_ok=True)

for i in range(start_page, end_page):
    page = reader.pages[i]
    count = 0
    for image_file_object in page.images:
        # Use page number in filename
        filename = f"{output_dir}/page_{i+1}_img_{count}.{image_file_object.name.split('.')[-1]}"
        with open(filename, "wb") as fp:
            fp.write(image_file_object.data)
        count += 1
    print(f"Extracted {count} images from page {i+1}")
