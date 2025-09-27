import openpyxl
import json

#Đọc dữ liệu từ file students.xlsx.
workbook = openpyxl.load_workbook("../python/BT_Buoi6/Data/students.xlsx")
sheet = workbook.active

# Khai báo mảng rỗng
students = []
    
# Lưu dữ liệu vào list of dict trong Python.
for row in sheet.iter_rows(min_row=2, values_only=True):
    student_id, name, score,rank=row
    students.append({
            "ID":student_id,
            "Họ tên": name,
            "Điểm": score,
            "Xếp loại": rank
    })
    print(row)
    
# Ghi dữ liệu này ra file report.json theo format JSON, giữ nguyên tiếng Việt.
with open("report.json", "w", encoding="utf-8") as f:
    json.dump(students, f, ensure_ascii=False, indent=4)
print("Đã tạo file report.json thành công!")