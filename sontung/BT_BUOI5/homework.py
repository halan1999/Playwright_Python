from datetime import datetime

# Bài 1
print('Bài 1:')
try:
    num = int(input("Nhập số: "))
    print("Bình phương: ", num ** 2)

except ValueError:
    print("Sai định dạng")

# Bài 2
print('\nBài 2:')
try:
    with open("data.txt", "r") as f:
        content = f.read()
        print("Nội dung:", content)

except FileNotFoundError:
    print("File không tồn tại")

finally:
    print("Kết thúc chương trình")

# Bài 3
print('\nBài 3:')
try:
    yearBirth = int(input("Nhập năm sinh: "))
    yearCurrent = datetime.now().year
    if yearBirth > yearCurrent:
        raise ValueError("Năm sinh không thể lớn hơn năm hiện tại")

except ValueError as e:
    print(f"Lỗi: {e}")

else:
    print(f"Tuổi: {yearCurrent - yearBirth}")
