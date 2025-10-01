import openpyxl
    #1. Mở file excel
workbook = openpyxl.load_workbook(r"C:\Users\Admin\Desktop\Python\BT_Buoi6\students.xlsx")
    #2.Chọn sheet
sheet = workbook.active
    #3. Đọc dữ liệu
for row in sheet.iter_rows(min_row=1, values_only= True):
    print(row)
#2
import json
students = [
    {"ID": "SV001", "Họ tên": "Nguyễn Văn An", "Điểm": 8.5, "Xếp loại": "Giỏi"},
    {"ID": "SV002", "Họ tên": "Trần Thị Bình", "Điểm": 9.0, "Xếp loại": "Xuất sắc"},
    {"ID": "SV003", "Họ tên": "Lê Văn Cường", "Điểm": 6.0, "Xếp loại": "Trung bình"},
    {"ID": "SV004", "Họ tên": "Phạm Thị Mai", "Điểm": 7.5, "Xếp loại": "Khá"}
]
with open("report.json", "w", encoding="utf-8") as f :
    json.dump(students, f, ensure_ascii= False, indent= 4)
    print("Tao file thanh cong")
