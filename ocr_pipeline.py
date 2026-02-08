import easyocr
import cv2
import numpy as np
import json
import re
import time
import os
import sys
from deep_translator import GoogleTranslator

reader = easyocr.Reader(['hi', 'en'])
translator = GoogleTranslator(source='auto', target='en')

def extract_text_boxes(image_path):
    result = reader.readtext(image_path)
    boxes = []
    for (bbox, text, prob) in result:
        cx = sum([p[0] for p in bbox]) / 4
        cy = sum([p[1] for p in bbox]) / 4
        boxes.append({
            'text': text,
            'bbox': bbox,
            'center': (cx, cy),
            'prob': prob
        })
    return boxes

def sort_boxes(boxes, image_width):
    header_threshold = 150
    header = []
    body_left = []
    body_right = []

    for box in boxes:
        cx, cy = box['center']
        if cy < header_threshold:
            header.append(box)
        elif cx < image_width / 2:
            body_left.append(box)
        else:
            body_right.append(box)

    header.sort(key=lambda b: (b['center'][1], b['center'][0]))
    body_left.sort(key=lambda b: b['center'][1])
    body_right.sort(key=lambda b: b['center'][1])

    return header + body_left + body_right

def clean_ocr_text(text):
    return text.strip()

def is_option_line(text):
    if re.match(r'^\(?[अ-हa-dA-D0-9]{1,2}\)', text):
        return True
    if re.match(r'^[अ-हa-dA-D]\s*\)', text):
        return True
    return False

def parse_questions(sorted_boxes, current_chapter, current_marks):
    questions = []
    current_q = None
    state = 0 # 0: Header, 1: Question, 2: Options
    q_text_buffer = []

    current_type = "MCQ" # Default

    # Regex for section headers
    header_mcq = re.compile(r'(?:वस्तुनिष्ठ|Objective|MCQ)')
    header_very_short = re.compile(r'(?:अतिलघु|Very Short)')
    header_short = re.compile(r'(?:लघु|Short)')
    header_fill = re.compile(r'(?:रिक्त|Fill|Blank)')

    # Regex for question start (number at start of line)
    q_start_pattern = re.compile(r'^(\d+|[lI\|])[\.\-\)]\s*')

    for box in sorted_boxes:
        text = clean_ocr_text(box['text'])

        # Chapter Update
        if "अध्याय" in text:
            nums = re.findall(r'\d+', text)
            if nums: current_chapter = nums[0]
            # Don't skip line, might contain other info

        # Section Type Update
        if header_very_short.search(text):
            current_type = "Very Short"
            current_marks = "1"
        elif header_short.search(text):
            current_type = "Short"
            current_marks = "2"
        elif header_fill.search(text):
            current_type = "Fill in the Blank"
            current_marks = "1"
        elif header_mcq.search(text):
            current_type = "MCQ"
            current_marks = "1"

        is_opt = is_option_line(text)
        is_q_start = q_start_pattern.match(text)

        # If we see an option line, force type to MCQ for this question
        if is_opt:
            current_type = "MCQ"

            if state == 1:
                # Finishing question text, starting options
                full_q_text = " ".join(q_text_buffer).strip()
                if full_q_text:
                    current_q = {
                        'Chapter': current_chapter,
                        'Questions type': current_type,
                        'Question in Hindi': full_q_text,
                        'Question in English': '',
                        'Answer in Hindi': '',
                        'Answer in English': '',
                        'Marks': current_marks,
                        'Options': []
                    }
                    current_q['Options'].append(text)
                    questions.append(current_q)
                    current_q = questions[-1]
                    q_text_buffer = []
                state = 2
            elif state == 2:
                if current_q: current_q['Options'].append(text)
            elif state == 0:
                pass

        else:
            # Not an option
            # Check if new question start (based on number)
            # Only reliably works if numbers are detected
            if is_q_start and len(text) > 3:
                # Start new question
                if current_q:
                    # Previous question finished?
                    # If state was 1 (accumulating text), finish it
                    if state == 1:
                        full_q_text = " ".join(q_text_buffer).strip()
                        if full_q_text:
                            # Save as question without options (yet)
                             prev_q = {
                                'Chapter': current_chapter,
                                'Questions type': current_type, # Use current type context
                                'Question in Hindi': full_q_text,
                                'Question in English': '',
                                'Answer in Hindi': '',
                                'Answer in English': '',
                                'Marks': current_marks,
                                'Options': []
                            }
                             questions.append(prev_q)

                    # If state was 2, options finished
                    current_q = None

                state = 1
                q_text_buffer = [text]

            else:
                # Continuation
                if state == 2:
                    # Transition from Options -> Question text (if no number detected)
                    # Heuristic: if long text, probably next question
                    if len(text) > 15:
                        state = 1
                        q_text_buffer = [text]
                        current_q = None
                    else:
                        # might be option part
                        if current_q: current_q['Options'].append(text)

                elif state == 1:
                    q_text_buffer.append(text)
                elif state == 0:
                    state = 1
                    q_text_buffer.append(text)

    # Finalize last buffer if any
    if state == 1 and q_text_buffer:
         full_q_text = " ".join(q_text_buffer).strip()
         if full_q_text:
             questions.append({
                'Chapter': current_chapter,
                'Questions type': current_type,
                'Question in Hindi': full_q_text,
                'Question in English': '',
                'Answer in Hindi': '',
                'Answer in English': '',
                'Marks': current_marks,
                'Options': []
            })

    return questions, current_chapter

def translate_and_finalize(questions):
    final_data = []
    for q in questions:
        ans_text_hi = ""

        # Only process Options if present
        if q.get('Options'):
            last_opt = q['Options'][-1]
            if re.match(r'^\([अ-ह]\)$', last_opt):
                key = last_opt.replace('(', '').replace(')', '')
                q['Answer in Hindi'] = key
                q['Options'].pop()

            for i, opt in enumerate(q['Options']):
                match = re.search(r'\s+\(([अ-ह])\)$', opt)
                if match:
                    key = match.group(1)
                    q['Answer in Hindi'] = key
                    ans_text_hi = opt.replace(match.group(0), '').strip()
                    q['Options'][i] = ans_text_hi
                    break

        if not q['Answer in Hindi']:
            match = re.search(r'\s+\(([अ-ह])\)$', q['Question in Hindi'])
            if match:
                key = match.group(1)
                q['Answer in Hindi'] = key
                q['Question in Hindi'] = q['Question in Hindi'].replace(match.group(0), '').strip()

        if q['Answer in Hindi'] and not ans_text_hi and q.get('Options'):
            key = q['Answer in Hindi']
            for opt in q['Options']:
                if opt.startswith(f"({key})") or f"({key})" in opt:
                    ans_text_hi = opt
                    break
            if not ans_text_hi: ans_text_hi = key

        q['Answer in Hindi'] = ans_text_hi

        try:
            if q['Question in Hindi']:
                q['Question in English'] = translator.translate(q['Question in Hindi'])
                time.sleep(0.5)
            if q['Answer in Hindi']:
                q['Answer in English'] = translator.translate(q['Answer in Hindi'])
                time.sleep(0.5)
        except Exception as e:
            print(f"Translation error: {e}")

        if 'Options' in q: del q['Options']
        final_data.append(q)

    return final_data

def main():
    start_page = int(sys.argv[1]) if len(sys.argv) > 1 else 31
    end_page = int(sys.argv[2]) if len(sys.argv) > 2 else 51

    output_file = 'political_science_questions.json' # Using final name directly
    all_data = []

    # If loading existing, check file
    # For this run, we overwrite to apply fixes
    if os.path.exists(output_file) and start_page > 31:
         try:
            with open(output_file, 'r', encoding='utf-8') as f:
                all_data = json.load(f)
         except: pass

    current_chapter = "13"
    current_marks = "1"

    for page_num in range(start_page, end_page):
        path = f'pages/page_{page_num}.png'
        if not os.path.exists(path):
            continue

        print(f"Processing {path}...")
        try:
            boxes = extract_text_boxes(path)
            img = cv2.imread(path)
            h, w, _ = img.shape
            sorted_boxes = sort_boxes(boxes, w)

            questions, next_chapter = parse_questions(sorted_boxes, current_chapter, current_marks)
            if next_chapter != "Unknown": current_chapter = next_chapter

            final_data = translate_and_finalize(questions)
            all_data.extend(final_data)

            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(all_data, f, ensure_ascii=False, indent=2)

        except Exception as e:
            print(f"Error processing {path}: {e}")

    print(f"Completed range {start_page}-{end_page}. Saved to {output_file}")

if __name__ == "__main__":
    main()
