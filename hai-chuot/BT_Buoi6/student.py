import openpyxl
import json

workbook = openpyxl.load_workbook("student.xlsx")
sheet = workbook.active
list_student = []

for row in sheet.iter_rows(min_row = 2, values_only=True):
    student_id, name, score, student_type = row
    
    list_student.append({
        "ID": student_id,
        "Họ và tên": name,
        "Điểm": score,
        "Xếp loại": student_type
    })

with open("student.json", "w", encoding="utf-8") as f:
    json.dump(list_student, f, ensure_ascii=False, indent=4)