from pypdf import PdfReader

reader = PdfReader("shekhawati-mission-100-samajik-vigyan-10th-2026.pdf")
# Extract text from page 31 (index 30)
page = reader.pages[30]
print(page.extract_text())
