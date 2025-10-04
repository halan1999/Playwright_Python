# NOTE Bài 1: Nhập số
# Viết chương trình yêu cầu người dùng nhập số.
# Nếu nhập đúng → in bình phương.
# Nếu nhập sai → in "Sai định dạng".

try:
    number_input = int(input("Hãy nhập một số mà bạn muốn bình phương: "))
    print(f"Bình phương của {number_input} = {number_input ** 2}")
except ValueError:
    print(f"Giá trị mà bạn vừa nhập đã sai định dạng!")