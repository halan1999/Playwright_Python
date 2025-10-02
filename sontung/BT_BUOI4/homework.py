# Bài 1
print('Bài 1: ')

text = " hello world "

print("Số kí tự ban đầu:", len(text))

print("Số kí tự sau:", len(text.strip()))

name = "tên bạn"

# Bài 2
print('\nBài 2: ')

name = "Sơn Tùng"

print(name.upper())

print(name.lower())

print(name.capitalize())

print(name.title())

# Bài 3
print('\nBài 3: ')

s = "Automation Testing"

print(s[:10])

print(s[11:])

print(s[:5])

print(s[-3:])

# Bài 4
print('\nBài 4: ')

messy_phone = " 090-123 4567 "

phone = messy_phone.replace(" ", "").replace("-", "")

print("SĐT sau khi chuẩn hóa: ", phone)

# Bài 5
print('\nBài 5: ')

fruits = ["apple", "banana", "cherry"]

print(", ".join(fruits))

# Bài 6
print('\nBài 6: ')

log = "ERROR: Login failed at 10:45"

if "ERROR" in log:
    print("Có lỗi xảy ra")
else:
    print("Hệ thống bình thường")
