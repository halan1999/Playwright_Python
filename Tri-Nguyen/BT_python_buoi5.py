#Bài 1
print("Bài 1 ------------")
x = 0
try:
    a  = int(input("nhập số vào: "))
    x = a ** 2
    print(f"bình phương của {a} là {x}")
except ValueError:
    print("bạn đã nhập sai định dạng")

#Bài 2
print("Bài 2 ------------")
def safe_divide(a, b):
    if b == 0:
        return "Không thể chia cho 0"
    else:
        return a / b
try:
    a = int(input("nhập số vào a: "))
    b = int(input("nhập số vào b: "))
    result = safe_divide(a, b)
    print("kết quả chia 2 số", a, "và", b, "là", result)
except ValueError:
    print("Bạn đã nhập sai định dạng (không phải số).")

#bài 3
print("bài 3 ----------")
try:
    f = open("data.txt", "r", encoding="utf-8")
except FileNotFoundError:
    print("file data.txt không tồn tại")
else:
    print("đọc file thành công")
    print(f.read())
    f.close()
finally:
    print("kết thúc chương trình")

#bài 4
print("bài 4 --------")
try:
    element = "submit"
    if element != "submit":
        raise Exception("không tìm thấy element")
    print("đã tìm thấy nút submit")
except:
    print("không tìm thấy element")
finally:
    print("đóng trình duyệt")

#Bài 6
current_year = 2025
try:
    birthday = int(input("nhập năm sinh của bạn: "))
    if birthday > 2025:
        raise TypeError("năm sinh không được lớn hơn năm hiện tại")
except ValueError:
    print("năm sinh không được là chữ")
except TypeError:
    print("năm sinh không được lớn hơn năm hiện tại")
else:
    age = current_year - birthday
    print(f"tuổi là {age}")
finally:
    print("kết thúc chương trình")