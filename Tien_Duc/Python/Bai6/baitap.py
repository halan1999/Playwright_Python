import json
import openpyxl
workbook = openpyxl.load_workbook('/Users/ducnt/Documents/Python/data/students.xlsx')
sheet = workbook.active
students = []
for row in sheet.iter_rows(min_row=2, values_only=True):
    id, name, score, level = row
    try:
        score_af = float(score)
        students.append({
        "ID": id,
        "Ten": name,
        "Diem": score_af,
        "Xep loai": level
    })
    except Exception as e:
        print("Loi, ly do:", e)
    
print(students)
with open('/Users/ducnt/Documents/Python/data/report.json', 'w', encoding='utf-8') as f:
    json.dump(students, f, ensure_ascii=False, indent=4)
