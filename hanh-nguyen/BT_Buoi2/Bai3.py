# Khai báo các biến
a = 10
b = 3.5
c = True
d = None 
e = "Python"

# In kiểu dữ liệu từng biến
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

# Tạo list scores
scores = [9, 7, 10, 8, 6]

# In điểm cao nhất
print(max(scores))

# Tính điểm trung bình
print(sum(scores)/len(scores))

# Thêm điểm 5 vào cuối list
scores.append(5)
print(scores)

# Tạo tuple DOB và in ngày, tháng, năm
birthday = (11, 9, 2025)
print("Ngày sinh:", birthday[0])
print("Tháng sinh:", birthday[1])
print("Năm sinh:", birthday[2])

# Thay đổi giá trị tuple
birthday[1] = 2