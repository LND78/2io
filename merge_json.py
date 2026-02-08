import json
import glob
import os

def normalize_chapter(chap):
    return str(chap)

def normalize_marks(mark):
    return str(mark)

def merge_jsons():
    merged_data = []
    # Generate range 31 to 50
    # Note: Use sorted list to maintain order
    page_files = [f"page_{i}.json" for i in range(31, 51)]

    existing_files = []
    for file_path in page_files:
        if os.path.exists(file_path):
            existing_files.append(file_path)
        else:
            print(f"Warning: {file_path} does not exist.")

    print(f"Merging files: {existing_files}")

    for file_path in existing_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if isinstance(data, list):
                    for item in data:
                        # Normalize Chapter
                        if "Chapter" in item:
                            item["Chapter"] = normalize_chapter(item["Chapter"])
                        # Normalize Marks
                        if "Marks" in item:
                            item["Marks"] = normalize_marks(item["Marks"])

                        merged_data.append(item)
                else:
                    print(f"Warning: {file_path} content is not a list. Skipping.")
        except Exception as e:
            print(f"Error reading {file_path}: {e}")

    output_file = "political_science_questions.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(merged_data, f, ensure_ascii=False, indent=2)
    print(f"Successfully merged {len(merged_data)} questions into {output_file}")

if __name__ == "__main__":
    merge_jsons()
