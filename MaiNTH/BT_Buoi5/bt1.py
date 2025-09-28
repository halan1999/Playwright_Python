#  Nhập số sử dụng try except.
# Viết chương trình yêu cầu người dùng nhập số.
# Nếu nhập đúng → in bình phương.
# Nếu nhập sai → in "Sai định dạng".
try:
    num = float(input("Vui long nhap mot so: "))
    print("Binh phuong cua so vua nhap la:", num ** 2)
except ValueError:
    print("Ban nhap khong phai là hieu  so.")
