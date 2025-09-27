try:
    a = int(input("Nhập a: "))
    b = int(input("Nhập b: "))
    c = a / b
    print(f"Kết quả: {a} / {b} = {c}")
except (ValueError,ZeroDivisionError)  :
    print("Lỗi rồi lỗi rồi !!!")

