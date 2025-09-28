# File location: Buoi2
# Viết chương trình Python để:
# Đọc dữ liệu từ file students.xlsx.
# Lưu dữ liệu vào list of dict trong Python.
# Ghi dữ liệu này ra file report.json theo format JSON, giữ nguyên tiếng Việt.

import openpyxl, json

workbook = openpyxl.load_workbook("../Python/BaiTap/students.xlsx")
sheet = workbook.active
students = []

print("\nStudents Information")
for row in sheet.iter_rows(min_row=2, values_only=True):
    studentId, studentName, studentScore, studentRank = row
    print(f"ID: {studentId}, Name: {studentName}, Score: {studentScore}, Rank: {studentRank}")

    students.append({
        "ID": studentId,
        "Full name": studentName,
        "Score": studentScore,
        "Rank": studentRank
    })
print(json.dumps(students, ensure_ascii=False, indent=5))

with open("BaiTap/Buoi6/students.json", "w", encoding="utf-8") as f:
    json.dump(students, f, ensure_ascii=True, indent=5)
print("JSON file created successfully!")
