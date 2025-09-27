# Nhập số
# Viết chương trình yêu cầu người dùng nhập số.
# Nếu nhập đúng → in bình phương.
# Nếu nhập sai → in "Sai định dạng".

try:
    num = int(input("Please input a: "))
    squaredNumber = num * num
    print(f"{num}^2 = {squaredNumber}")
except ValueError as e:
    print(f"Error: Invalid format")