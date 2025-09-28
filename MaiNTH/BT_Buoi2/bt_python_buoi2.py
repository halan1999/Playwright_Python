# 1. Tao list gồm 5 số, tính tổng tất cả các số trong list và in ra kết quả
numbers = [10, 20, 30, 40, 50]
total = sum(numbers)
print("1.Tong cac so trong list:", total)
# 2. Viết chương trình in ra tất cả các phẩn từ của dict {"name": "Lan", "age": 25, "city": "Hà Nội "}
info = {"name": "Lan", "age": 25, "city": "Hà Nội"}
for key, value in info.items():
    print(f"{key}: {value}")
# 3. Khai báo các biến sau:
a = 10
b = 3.5 
c = True
d = None
e = "Python"    
# In ra kiểu dữ liệu của các biến trên
print("3.Kieu du lieu cua cac bien:")
print("a:", type(a))
print("b:", type(b))
print("c:", type(c))
print("d:", type(d))
print("e:", type(e))
# Tạo list scores
scores = [9, 7, 10, 8, 6]
# In ra điểm cao nhất
print("Diem cao nhat:", max(scores))
# Tính điểm trung bình
print("Diem trung binh:", sum(scores) / len(scores))
# Thêm điểm 5 vào cuối list
scores.append(5)
# Tạo birthday tuple
birthday = (11, 9, 2025)
print("Birthday:", birthday)


# 4. Tạo dict student
student = {
    "name": "Lan",
    "age": 18,
    "email": "lan@gmail.com"
}
# In ra tên và email của student
print("4.Ten:", student["name"])
print("Email:", student["email"])
# 5. Tạo set email
emails = {"@gmail.com","b@gmail.com","c@gmail.com"}
# In ra số lượng email trong set
print("5.So luong email trong set:", len(emails))
# Thêm email "
emails.add("c@gmail.com")
print("Set email sau khi them:", emails)
