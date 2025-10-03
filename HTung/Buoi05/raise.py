try:
    password = input("Nhap mat khau: ")
    if len(password) < 6:
        raise ValueError("Mat khau khong hop le! ít nhat 6 ky tu")
except ValueError as e:
    print(e)