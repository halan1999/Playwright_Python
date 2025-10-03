# Bài 1: Nhập số
# Viết chương trình yêu cầu người dùng nhập số.

# Nếu nhập đúng → in bình phương.

# Nếu nhập sai → in "Sai định dạng".

try:
    number_input = float(input("Nhập một số:")) # có thể ép kiểu int hoặc float, nhưnng dung float thì nó có tính linh hoạt hơn

    result = number_input ** 2
except ValueError:
    print("Đang sai đinh dạng")
else:
    print(f"Kết quả:{number_input} ^ 2 = {result}")

#(*) khi dùng int mà chúng ta nhập dạng 1.5 thì sẻ đi xuống ValueError