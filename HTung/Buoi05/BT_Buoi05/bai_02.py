# Bài 2: Máy tính an toàn
# Viết hàm safe_divide(a, b) chia 2 số.

# Nếu b = 0 → trả về "Không thể chia cho 0".

# Ngược lại → trả về kết quả.

try:
    input_a = input("Nhap a: ")
    input_b = input("Nhap b: ")

    a = float(input_a)
    b = float(input_b)

    safe_divide = a/b
except ValueError:
    print("Dữ liệu không hợp")
except  ZeroDivisionError:
    print("Không thể chia cho 0")
else:
    print("Kết quả: ",safe_divide)