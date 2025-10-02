# Khai báo biến
a = 10
b = 3.5
c = True
d = None
e = "Python"
# in ra kiểu dữ liệu cho từng biến 
print(type(a), type(b), type(c), type(d), type(e))

#Tạo 1 list có tên scores
scores = [9, 7, 10, 8, 6]
#Lấy điểm cao nhất
print("Điểm cao nhất là:", max(scores))

#Tỉnh điểm trung bình trong scores
print("Điểm trung bình là:", sum(scores))

#Thêm điểm 5 vào cuối list
scores.append(5)
# in lại giá trị thêm vào list
print(scores)

#Tạo tuple birthday
birthday = (11, 9, 2025)
print("Ngày:",birthday[0],",Tháng:",birthday[1],",Năm:",birthday[2])