import openpyxl, json
workbook = openpyxl.load_workbook("..//EXERCISE_PYTHON/students.xlsx")
sheet = workbook.active
# Khởi tạo danh sách students
students = []

for row in sheet.iter_rows(min_row=2, values_only=True):
    student_id, name, score, grade = row
    try:
        score_af = float(score)
    except Exception as e:
        print("Error: ", e)
    students.append(
    {
        "ID": student_id,
        "Họ tên": name,
        "Điểm": score_af,
        "Xếp loại": grade
    })    

with open("report.json", "w", encoding="utf-8") as f:
    json.dump(students, f, ensure_ascii=False, indent=4)
print("✅ Đã tạo file report.json thành công!")