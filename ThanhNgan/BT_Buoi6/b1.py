import openpyxl, json

try:
    workbook = openpyxl.load_workbook("./data/students.xlsx")
    sheet = workbook.active
    students = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        student_id, name, score, rank = row
        try:
            score = float(score)
        except Exception as E:
            print(f"Lỗi: {E}")
        students.append({
            "ID":student_id,
            "Họ tên": name,
            "Điểm": score,
            "Xếp loại": rank
        })
    with open(file="./report.json", mode="w", encoding="utf-8") as f:
        json.dump(students, f, ensure_ascii=False, indent=4)
    print("Xuất dữ liệu thành công")
except FileNotFoundError:
    print("Lỗi không tìm thấy file")
except Exception as e:
    print(f"Lỗi: {e}")