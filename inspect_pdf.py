import pdfplumber

with pdfplumber.open("shekhawati-mission-100-samajik-vigyan-10th-2026.pdf") as pdf:
    # Pages 51-65 means indices 50 to 64 if 1-based, or maybe printed page numbers.
    # Let's extract text from indices 50 to 52 to verify content.
    for i in range(50, 55): # Check a few pages around 51
        page = pdf.pages[i]
        text = page.extract_text()
        print(f"--- Page Index {i} (Page {i+1}) ---")
        print(text[:500]) # Print first 500 chars
        print("\n")
