# Viết hàm safe_divide(a, b) chia 2 số.
# Nếu b = 0 → trả về "Không thể chia cho 0".
# Ngược lại → trả về kết quả.

try:
    a = float(input("Hãy nhập vào số a: "))
    b = float(input("Hãy nhập vào số b: "))
    safe_divide = a/b
    print("Kết quả phép chia a cho b là:", safe_divide)
except ZeroDivisionError:
    print("Không thể chia cho 0")