# NOTE Bài 2: Máy tính an toàn
# Viết hàm safe_divide(a, b) chia 2 số.
# Nếu b = 0 → trả về "Không thể chia cho 0".
# Ngược lại → trả về kết quả.

def safe_divide(a, b):
    try:
        result = a/b
    except ZeroDivisionError:
        print("Không thể chia cho 0!")
    else:
        print(f"Kết quả của phép tính là: {result}")
    finally:
        print("KẾT THÚC CHƯƠNG TRÌNH!")

try:
    input_a = int(input("Nhập a: "))
    input_b = int(input("Nhập b: "))
except ValueError:
    print(f"Giá trị mà bạn vừa nhập đã sai định dạng!")
    print("KẾT THÚC CHƯƠNG TRÌNH!")
else:
    safe_divide(input_a, input_b)