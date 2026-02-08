from pypdf import PdfReader

reader = PdfReader("shekhawati-mission-100-samajik-vigyan-10th-2026.pdf")

for i in range(50, 55):
    page = reader.pages[i]
    text = page.extract_text()
    print(f"--- Page Index {i} (Page {i+1}) ---")
    print(text[:500])
    print("\n")
