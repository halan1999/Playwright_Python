try:
    # Yêu cầu người dùng nhập số
    number = float(input("Nhập một số: "))
    
    # Nếu nhập đúng thì in ra bình phương
    print("Bình phương là:", number ** 2)

except ValueError:
    # Nếu nhập sai (không phải số) thì báo lỗi
    print("Sai định dạng")
