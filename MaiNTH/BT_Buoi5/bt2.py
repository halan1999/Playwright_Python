# File
# Đọc file data.txt.
# Nếu file tồn tại → in nội dung.
# Nếu không → in "File không tồn tại".
# Luôn in "Kết thúc chương trình".
try:
    with open("D:\PYTHON\BT_Buoi5\data.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print("Noi dung file:")
        print(content)
except FileNotFoundError:
    print("File khong ton tai.")
finally:
    print("Ket thuc chuong trinh.")
