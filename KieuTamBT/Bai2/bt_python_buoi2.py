# Bài 1: Tạo list gồm 5 số, tính tổng tất cả các số trong list.
# Tạo list gồm 5 số
numbers = [8, 9, 20, 46, 33]

# Tính tổng bằng hàm sum
total = sum(numbers)

print("***********Bài tập 1:***********")
print("Danh sách:", numbers)
print("Tổng các số trong list là:", total)

# Bài 2: Viết chương trình in ra tất cả các phần tử của dict {"name": "Lan", "age": 25, "city": "Hà Nội"}
person = {"name": "Lan", "age": 25, "city": "Hà Nội"}

# Bài 3
# Khai báo biến
a = 10
b = 3.5
c = True
d = None
e = "Python"

# In ra kiểu dữ liệu của từng biến
print("*********Kết quả của bài 3: ************")
print("Kiểu dữ liệu của a:", type(a))
print("Kiểu dữ liệu của b:", type(b))
print("Kiểu dữ liệu của c:", type(c))
print("Kiểu dữ liệu của d:", type(d))
print("Kiểu dữ liệu của e:", type(e))

print("\n--- Làm việc với List ---")
# Tạo list scores
scores = [9, 7, 10, 8, 6]

# In ra điểm cao nhất
print("Điểm cao nhất:", max(scores))

# Tính điểm trung bình
average = sum(scores) / len(scores)
print("Điểm trung bình:", average)

# Thêm điểm 5 vào cuối list
scores.append(5)
print("Danh sách sau khi thêm:", scores)

print("\n--- Làm việc với Tuple ---")
# Tạo tuple birthday
birthday = (11, 9, 2025)
print("Ngày:", birthday[0])
print("Tháng:", birthday[1])
print("Năm:", birthday[2])

# Thử thay đổi giá trị trong tuple (sẽ gây lỗi)
print("Lỗi khi thay đổi tuple: birthday[0] = 12 ")
#birthday[0] = 12

#Bài 4:
# Tạo dictionary
student = {"name": "Lan", "age": 18, "email": "lan@gmail.com"}

# In ra tên và email
print("***********Kết quả của bài 4: In ra tên và email**********")
print("Tên:", student["name"])
print("Email:", student["email"])

# Bài 5
# Tạo set
emails = {"a@gmail.com", "b@gmail.com", "a@gmail.com"}
print("***********Kết quả của bài 5 **********")
print("Khi in set ra:", emails)

# Thêm phần tử mới
emails.add("c@gmail.com")
print("Sau khi thêm c@gmail.com:", emails)

# Thử xóa "d@gmail.com" bằng remove
try:
    emails.remove("d@gmail.com")
except KeyError as e:
    print("Lỗi khi dùng remove:", e)

# Thử xóa "d@gmail.com" bằng discard
emails.discard("d@gmail.com")
print("Sau khi dùng discard với d@gmail.com:", emails)