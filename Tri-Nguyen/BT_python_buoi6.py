import openpyxl, json
workbook = openpyxl.load_workbook("../data/bai6.xlsx")
sheet = workbook.active
students = []
#đọc dữ liệu trong file xlsx
print("đọc dữ liệu file xlsx ------------")
for row in sheet.iter_rows(min_row=2, values_only=True):
    try:
        Stt, Username, Scores, Arrange_Range = row
        print(row)
    except Exception as e:
        print(f"lỗi: {e}")
#in file xlsx vào json
    students.append({
        "ID":Stt,
        "Họ Tên":Username,
        "Điểm":Scores,
        "Xếp loại":Arrange_Range
    })
#print(students)
#tạo file json
with open("report.json","w",encoding="utf-8") as f:
    json.dump(students,f,ensure_ascii=False, indent=4)
print("tạo file json thành công")
print("đọc file report.json ---------------")
with open('../data/report.json','r',encoding='utf-8') as f:
    try:
        report = json.load(f)
        #in toàn bộ dữ liệu từ file baitap.json
        print(report)
    except Exception as e:
        print(f"lỗi: {e}")