#1.Chương trình nhập số
# try:
#     so_input = input("Nhap so:")
#     so = int(so_input)
#     print("In so binh thuong:")
# except ValueError :
#     print("Sai dinh dang")
#2.File
#2.1
# try:
#     op = open("data.text","r")
# except FileNotFoundError:
#     print("Loi: khong tim thay file data.text")
# else:
#     print("Doc file thanh cong")
# finally:
#     print("Ket thuc chuong trinh")
# #2.2
# try:
#     with open("data.txt", "r") as r:
#         print(r.readlines())
# except FileNotFoundError:
#     print("File khong ton tai")
# finally:
#     print("Ket thuc chuong trinh")

# try:
#     file = open("data.txt","r")
#     data = file.read()
#     print("Noi dung file là:",data)
# except FileNotFoundError:
#     print("File khong ton tai")
# finally:
#     print("Ket thuc chuong trinh")
#3.Xử lý ValueError và lỗi logic với raise
try:
    year_input = input("Nhap năm sinh:")
    year = int(year_input)
    from datetime import datetime # Khai báo thư viện
    current_year = datetime.now().year
    if year > current_year:
        raise ValueError ("Nam sinh khong lon hon nam hien tai")
except ValueError as e :
    print("Loi", e)
else :
    year = current_year - year
    print("Tuoi cua ban la:", year)