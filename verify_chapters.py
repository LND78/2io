import json

with open("political_science_questions.json", "r") as f:
    data = json.load(f)

chapters = set()
for item in data:
    if "Chapter" in item:
        chapters.add(item["Chapter"])
    else:
        print("Missing Chapter field in item:", item)

print("Chapters found:", sorted(list(chapters), key=lambda x: int(x) if x.isdigit() else x))
