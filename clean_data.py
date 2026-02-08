
import json
import re
from deep_translator import GoogleTranslator

def fix_json():
    with open("geography_questions.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    fixed_data = []
    current_chapter = "1" # Start with 1 (Resource and Development)

    # Regex to find Chapter in text
    # e.g. "अध्याय - 9" or "अध्याय 4"
    chapter_in_text_pattern = re.compile(r"अध्याय\s*[-–]?\s*(\d+)")

    # Regex to find embedded Answer
    # e.g. "? उ ..." or "? उत्तर ..." or "? Ans ..."
    # Also handle if it's not after ? but just at end
    # Relaxed to handle 'उ' without dot
    embedded_ans_pattern = re.compile(r"(?:\?|l|\|)\s*(?:उ[\.]?|उत्तर|Ans|Uttar)[\s:-]+(.*)$", re.IGNORECASE)

    translator = GoogleTranslator(source='hi', target='en')

    for q in data:
        q_text_hi = q["Question in Hindi"]
        q_text_en = q["Question in English"]
        a_text_hi = q["Answer in Hindi"]
        a_text_en = q["Answer in English"]

        # 1. Check for Chapter change in Question text
        match_chap = chapter_in_text_pattern.search(q_text_hi)
        if match_chap:
            current_chapter = match_chap.group(1)
            # Remove the header from question text?
            # It might be at the start or middle.
            # "लिए शेखावाटी मिशन- १०० अध्याय - 9 रिक्तस्थान रिक्त स्थानों की पूर्ति कीजिए-"
            # We can try to clean it up, but it's risky.
            # Let's just update the Chapter field.

        # Update Chapter if it was Unknown
        if q["Chapter"] == "Unknown":
            q["Chapter"] = current_chapter
        else:
            current_chapter = q["Chapter"] # If valid, update state

        # 2. Check for embedded Answer if Answer field is empty
        if not a_text_hi.strip():
            match_ans = embedded_ans_pattern.search(q_text_hi)
            if match_ans:
                ans_text = match_ans.group(1).strip()
                # Remove answer from question text
                # We need to find where it starts
                # match_ans.start() gives index of match
                # match group 1 is the content.
                # We want to keep question text until the answer marker.

                # Re-match to include marker in the cut
                full_match = match_ans.group(0) # e.g. "? उ ..."
                start_idx = q_text_hi.find(full_match)

                if start_idx != -1:
                    # Keep text before answer, include punctuation if desired
                    # The regex includes the punctuation in the match (? or |)
                    # We might want to keep the punctuation in the question.
                    # full_match[0] is the punctuation.

                    split_point = start_idx + 1 # Keep punctuation

                    new_q_text_hi = q_text_hi[:split_point].strip()
                    new_a_text_hi = ans_text

                    q["Question in Hindi"] = new_q_text_hi
                    q["Answer in Hindi"] = new_a_text_hi

                    # Update English
                    try:
                        q["Question in English"] = translator.translate(new_q_text_hi)
                        q["Answer in English"] = translator.translate(new_a_text_hi)
                    except:
                        pass

        # 3. Clean up english translation if it contains "Chapter ..." from previous bad parse
        # Not easy to do automatically.

        fixed_data.append(q)

    with open("geography_questions_fixed.json", "w", encoding="utf-8") as f:
        json.dump(fixed_data, f, indent=2, ensure_ascii=False)

    print("Fixed JSON saved to geography_questions_fixed.json")

if __name__ == "__main__":
    fix_json()
