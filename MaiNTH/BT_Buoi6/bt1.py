# Bài toán: 
# Đọc dữ liệu từ file students.xlsx.
# Lưu dữ liệu vào list of dict trong Python.
# Ghi dữ liệu này ra file report.json theo format JSON, giữ nguyên tiếng Việt.
import openpyxl
import json

try:
    # 1. Mở file Excel
    workbook = openpyxl.load_workbook(r'BT_Buoi6\students.xlsx')
    # 2. Chọn sheet đầu tiên
    sheet = workbook.active
    # 3. Đọc từng dòng dữ liệu từ sheet và lưu vào list of dict
    students = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        try:
            student_id, name, score, level = row
            student = {
                'id': student_id,
                'name': name,
                'score': score,
                'level': level
            }
            students.append(student)
        except ValueError as e:
            print("Đã xảy ra lỗi:", e)
    print(students)
    # 4. Ghi dữ liệu ra file JSON
    with open('report.json', 'w', encoding='utf-8') as f:
        json.dump(students, f, ensure_ascii=False, indent=4)
        print("Đã ghi dữ liệu ra file report.json")
except FileNotFoundError:
    print("Không tìm thấy file students.xlsx")
except Exception as e:
    print("Đã xảy ra lỗi:", e)


