# Cho 1 file Excel tên students.xlsx có cấu trúc như sau:			
# ID	Họ tên	Điểm	Xếp loại
# SV001	Nguyễn Văn An	8.5	Giỏi
# SV002	Trần Thị Bình	9.0	Xuất sắc
# SV003	Lê Văn Cường	6.0	Trung bình
# SV004	Phạm Thị Mai	7.5	Khá
			
# "Viết chương trình Python để:

# Đọc dữ liệu từ file students.xlsx.

# Lưu dữ liệu vào list of dict trong Python.

# Ghi dữ liệu này ra file report.json theo format JSON, giữ nguyên tiếng Việt."			

import openpyxl,json
# Đọc dữ liệu từ file excel
wb=openpyxl.load_workbook("../python/data/students.xlsx")
sheet=wb.active
students=[]
#add vào dic
for row in sheet.iter_rows(min_row=2,values_only=True):
    student_id, name,score, level= row
    try :
       score_af=float(score)
    except Exception as e:
       print(f"loi: ",e)
    students.append(
    {"Mã Sinh Viên":student_id,
     "Họ và Tên":name,
     "Điểm":score_af,
     "Xếp hạng":level}
    )
print(students)
# Chuyển thành json

with open("students.json","w", encoding="utf-8") as f:
   json.dump(students,f,ensure_ascii=False,indent=4)
   print("Tạo thành công")
#mở kiểm tra file json
with open("students.json","r",encoding="utf-8") as f:
   data=json.load(f)
   print(data)

        
    
    



                 

