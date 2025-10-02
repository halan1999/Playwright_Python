import json
with open("food.json","r", encoding="utf-8") as f:
    try:
        cooking=json.load(f)
        print(cooking)
    except Exception as e:
        print("file error:",e)