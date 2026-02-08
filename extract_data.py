
import easyocr
from pypdf import PdfReader
from io import BytesIO
from PIL import Image
import numpy as np
import re
import json
import argparse
from deep_translator import GoogleTranslator

def extract_text_from_page(reader_ocr, page):
    if not page.images:
        return []

    img_obj = page.images[0]
    img_data = img_obj.data
    image = Image.open(BytesIO(img_data))

    width, height = image.size
    mid_point = width // 2

    # Split
    left_img = image.crop((0, 0, mid_point, height))
    right_img = image.crop((mid_point, 0, width, height))

    # OCR
    # detail=0 returns just text list
    left_text = reader_ocr.readtext(np.array(left_img), detail=0)
    right_text = reader_ocr.readtext(np.array(right_img), detail=0)

    return left_text + right_text

def parse_questions(all_lines):
    questions = []
    current_chapter = "Unknown"
    current_q_type = "Unknown"
    current_marks = "Unknown"

    current_q_text_hi = []
    current_a_text_hi = []
    current_q_num = None

    # Regex patterns
    chapter_pattern = re.compile(r"अध्याय\s*(\d+)")
    q_num_pattern = re.compile(r"^(\d+)[\.|)]")
    ans_start_pattern = re.compile(r"^(?:उ\.|उत्तर|Ans|Uttar)[\s:-]*", re.IGNORECASE)

    for line in all_lines:
        line = line.strip()
        if not line:
            continue

        # Check for Chapter
        match_chapter = chapter_pattern.search(line)
        if match_chapter:
            current_chapter = match_chapter.group(1)
            continue

        # Check for Question Type / Marks updates
        if "वस्तुनिष्ठ" in line:
            current_q_type = "MCQ"
            current_marks = "1"
        elif "रिक्त स्थान" in line:
            current_q_type = "Fill in the blank"
            current_marks = "1"
        elif "अतिलघु" in line or "अति लघु" in line:
            current_q_type = "Very Short Answer"
            current_marks = "1"
        elif "लघुतरात्मक" in line:
            current_q_type = "Short Answer"
            if "अंक-२" in line or "अंक - 2" in line or "अंक-2" in line:
                current_marks = "2"
            elif "अंक-3" in line or "अंक - 3" in line or "अंक-3" in line:
                current_marks = "3"
            else:
                current_marks = "2"
        elif "निबंधात्मक" in line:
            current_q_type = "Long Answer"
            current_marks = "4"

        # Check for Answer
        match_ans = ans_start_pattern.match(line)
        if match_ans:
            ans_text = ans_start_pattern.sub("", line).strip()
            current_a_text_hi.append(ans_text)
            continue

        # Check for New Question
        match_q = q_num_pattern.match(line)
        if match_q:
            if current_q_num is not None:
                q_obj = {
                    "Chapter": current_chapter,
                    "Questions type": current_q_type,
                    "Question in Hindi": " ".join(current_q_text_hi),
                    "Answer in Hindi": " ".join(current_a_text_hi),
                    "Marks": current_marks
                }
                questions.append(q_obj)

            current_q_num = match_q.group(1)
            current_q_text_hi = [line]
            current_a_text_hi = []
            continue

        if current_a_text_hi:
            current_a_text_hi.append(line)
        elif current_q_text_hi:
            if "अंक" in line and len(line) < 15:
                continue
            current_q_text_hi.append(line)

    if current_q_num is not None:
        q_obj = {
            "Chapter": current_chapter,
            "Questions type": current_q_type,
            "Question in Hindi": " ".join(current_q_text_hi),
            "Answer in Hindi": " ".join(current_a_text_hi),
            "Marks": current_marks
        }
        questions.append(q_obj)

    return questions

def translate_and_format(questions):
    translator = GoogleTranslator(source='hi', target='en')

    final_questions = []
    total = len(questions)
    for idx, q in enumerate(questions):
        if idx % 5 == 0:
            print(f"Translating question {idx + 1}/{total}...")

        q_hi = q["Question in Hindi"]
        a_hi = q["Answer in Hindi"]

        q_en = q_hi
        a_en = a_hi

        if q_hi.strip():
            try:
                q_en = translator.translate(q_hi)
            except Exception as e:
                print(f"Error translating Q {idx+1}: {e}")

        if a_hi.strip():
            try:
                a_en = translator.translate(a_hi)
            except Exception as e:
                print(f"Error translating A {idx+1}: {e}")

        final_q = {
            "Chapter": q["Chapter"],
            "Questions type": q["Questions type"],
            "Question in English": q_en,
            "Question in Hindi": q_hi,
            "Answer in English": a_en,
            "Answer in Hindi": a_hi,
            "Marks": q["Marks"]
        }
        final_questions.append(final_q)

    return final_questions

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf_path", help="Path to the PDF file")
    parser.add_argument("--start", type=int, default=15, help="Start page index")
    parser.add_argument("--end", type=int, default=30, help="End page index")
    args = parser.parse_args()

    pdf_path = args.pdf_path
    reader = PdfReader(pdf_path)
    reader_ocr = easyocr.Reader(['en', 'hi'])

    all_lines = []

    print(f"Processing pages {args.start + 1} to {args.end}...")

    for i in range(args.start, args.end):
        print(f"Processing page {i + 1}...")
        try:
            page = reader.pages[i]
            lines = extract_text_from_page(reader_ocr, page)
            all_lines.extend(lines)
        except Exception as e:
            print(f"Error processing page {i+1}: {e}")

    print(f"Extracted {len(all_lines)} lines of text.")
    print("Parsing extracted text...")
    questions = parse_questions(all_lines)

    print(f"Found {len(questions)} questions. Starting translation...")
    final_data = translate_and_format(questions)

    filename = f"geography_questions_{args.start}_{args.end}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(final_data, f, indent=2, ensure_ascii=False)

    print(f"Done. Saved to {filename}")

if __name__ == "__main__":
    main()
