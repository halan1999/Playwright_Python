import openpyxl, json
workbook = openpyxl.load_workbook("../Python/students_score.xlsx")
sheet = workbook.active
students = []
for row in sheet.iter_rows(min_row=2, values_only=True):
    student_id, name, score, rank = row
    try:
        score_af = float(score)
    except Exception as e:
        print(e)
    students.append({
        "ID": student_id,
        "Họ tên": name,
        "Điểm": score_af,
        "Xếp loại": rank
    })  
# print(students)
with open("report.json", "w", encoding="utf-8") as f:
    json.dump(students, f, ensure_ascii=False, indent=4)
print("Tao file json thanh cong")