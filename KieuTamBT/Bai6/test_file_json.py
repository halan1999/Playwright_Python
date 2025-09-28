import openpyxl, json
workbook = openpyxl.load_workbook("..//EXERCISE_PYTHON/Score_Student.xlsx")
sheet = workbook.active
# Khởi tạo ds sv
students = []
for row in sheet.iter_rows(min_row=2, values_only=True):
    stt, student_id, name, score = row
    try:
        score_af = float(score)
        stt_af = int(stt)
    except Exception as e:
        print("Error: ", e)
    if score_af >= 9:
        students.append(
        {
            "ID": student_id,
            "name": name,
            "level": "Very good"
        })
# print(students)
with open("report.json", "w", encoding="utf-8") as f:
    json.dump(students, f, ensure_ascii=False, indent=4)
print("✅ Đã tạo file report.json thành công!")