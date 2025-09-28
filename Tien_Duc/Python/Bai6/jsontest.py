import json
with open("../Python/Foods.json", "r", encoding="utf-8") as f:
    try:
        cookingway = json.load(f)
        print(cookingway)
    except Exception as e:
        print("Loi, ly do:", e)