#Khai báo để import đọc và ghi
import openpyxl
import json
try:
    # Thực hiện mở file .xlsx
    openfile = openpyxl.load_workbook("students.xlsx")

    # Chọn sheet data muốn thực hiện
    sheet_file = openfile.active
    # Đọc dữ liệu từ file 


    # Khởi tạo list chứa dict
    students = [
        # {"ID": "SV001", "Họ tên": "Nguyễn Văn An", "Điểm": 8.5, "Xếp loại": "Giỏi"},
        # {"ID": "SV002", "Họ tên": "Trần Thị Bình", "Điểm": 9.0, "Xếp loại": "Xuất sắc"},
        # {"ID": "SV003", "Họ tên": "Lê Văn Cường", "Điểm": 6.0, "Xếp loại": "Trung bình"},
        # {"ID": "SV004", "Họ tên": "Phạm Thị Mai", "Điểm": 7.5, "Xếp loại": "Khá"}
    ]
    for row in sheet_file.iter_rows(min_row=1 ,values_only=True) :
        print(row)
        student_id, name ,score, grade = row
        students.append({
            "ID": student_id,
            "Họ tên": name,
            "Điểm": score,
            "Xếp loại": grade
        })
    with open("report.json","w",encoding="utf-8") as g:
        json.dump(students, g, ensure_ascii=False , indent= 4)
        print("Đã tạo file")
except ValueError as e:
    print(e)