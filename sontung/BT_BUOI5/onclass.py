# Bài 1
print('Bài 1:')
try:
    num = int(input("Nhập số: "))
    print("Kết quả bình phương: ", num ** 2)

except ValueError:
    print("Sai định dạng")

# Bài 2
print('\nBài 2:')

def safe_divide(a, b):
    try:
        return a / b

    except ZeroDivisionError:
        return "Không thể chia cho 0"

print("Kết quả phép chia: ", safe_divide(7, 2))

# Bài 3
print('\nBài 3:')
try:
    with open("data.txt", "r") as f:
        content = f.read()
        print("Nội dung:", content)

except FileNotFoundError:
    print("File không tồn tại")

finally:
    print("Kết thúc chương trình")

# Bài 4
print('\nBài 4:')
element = str(input('Nhập element: '))
try:
    if not element:
        raise ValueError(f"Không tìm thấy element")
    else:
        print(f"Tìm thấy {element}")
except ValueError as e:
    print(e)
finally:
    print("Đóng trình duyệt!")