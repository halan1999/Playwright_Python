import openpyxl, json

workbook = openpyxl.load_workbook("../data/students.xlsx")
sheet = workbook.active

students = []

for row in sheet.iter_rows(min_row=2, values_only=True):
    student_id, name, score, rank = row

    students.append({
        "ID": student_id,
        "Họ tên": name,
        "Điểm": score,
        "Xếp loại": rank
    })

print(students)

with open('../data/report.json', 'w', encoding='utf-8') as f:
    json.dump(students, f, ensure_ascii=False, indent=4)   #indent: thụt lề cho file json

print("Ghi file json thành công!")