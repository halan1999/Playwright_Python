# Viết hàm safe_divide(a, b) chia 2 số.

# Nếu b = 0 → trả về "Không thể chia cho 0".

# Ngược lại → trả về kết quả.
def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Không thể chia cho 0."
print(safe_divide(10, 2))  # Output: 5.0
print(safe_divide(10, 0))  # Output: "Không thể chia cho 0."