# "Bài 1: Nhập số
# Viết chương trình yêu cầu người dùng nhập số.

# Nếu nhập đúng → in bình phương.

# Nếu nhập sai → in ""Sai định dạng""."

try:
    number = float(input("Mời nhập số: "))
except (ValueError, TypeError) as e:
    print("Sai định dạng", e)
else:
    print(f"Bình phương của {number} = {number**2:.2f}")