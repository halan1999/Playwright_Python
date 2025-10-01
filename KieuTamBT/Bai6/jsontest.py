import json

with open("food.json", "r", encoding="utf-8") as f:
    try:
        cookingway = json.load(f)
        print(cookingway)
    except Exception as e:
        print("File error: ", e)