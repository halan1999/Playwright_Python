# Tạo list gồm 5 số
numbers = [8, 9, 16, 28, 30]

# Tính tổng tất cả các số trong list
total = sum(numbers)

# In kết quả
print("Tổng các số trong list là:", total)

# Tạo dict
person = {"name": "Hao", "age": 25, "city": "Nghệ An"}
# In list
print(person)

# In ra tất cả các phần tử của dict
# for key, value in person.items():
    # print(key, ":", value)
# Khai báo biến
a = 10
b = 3.5
c = True
d = None
e = "Python"

# In ra kiểu dữ liệu của từng biến
print("Kiểu dữ liệu của a:", type(a))
print("Kiểu dữ liệu của b:", type(b))
print("Kiểu dữ liệu của c:", type(c))
print("Kiểu dữ liệu của d:", type(d))
print("Kiểu dữ liệu của e:", type(e))

print("\n--- Làm việc với list ---")
scores = [9, 7, 10, 8, 6]

# In ra điểm cao nhất
print("Điểm cao nhất:", max(scores))

# Tính điểm trung bình
average = sum(scores) / len(scores)
print("Điểm trung bình:", average)

# Thêm điểm 5 vào cuối list
scores.append(5)
print("Danh sách sau khi thêm điểm 5:", scores)

print("\n--- Làm việc với tuple ---")
birthday = (11, 9, 2025)

# In ra ngày, tháng, năm
day, month, year = birthday
print("Ngày:", day)
print("Tháng:", month)
print("Năm:", year)

# Thử thay đổi giá trị trong tuple (sẽ lỗi)
try:
    birthday[0] = 12
except TypeError as e:
    print("Lỗi khi thay đổi tuple:", e)

# Tạo dictionary
student = {"name": "Hao", "age": 25, "email": "haodt301299@gmail.com"}

# In ra tên và email
print("Tên:", student["name"])
print("Email:", student["email"])
# Tạo set
emails = {"a@gmail.com", "b@gmail.com", "a@gmail.com"}

# Quan sát kết quả khi in set ra sẽ loại bỏ giá trị trùng lặp
print("Set ban đầu:", emails)

# Thêm "c@gmail.com"
emails.add("c@gmail.com")
print("Sau khi thêm c@gmail.com:", emails)

# Thử xóa "d@gmail.com" bằng remove (sẽ lỗi nếu phần tử không tồn tại)
try:
    emails.remove("d@gmail.com")
except KeyError as e:
    print("Lỗi khi remove:", e)

# Thử xóa "d@gmail.com" bằng discard (không lỗi nếu phần tử không tồn tại)
emails.discard("d@gmail.com")
print("Sau khi discard d@gmail.com:", emails)

