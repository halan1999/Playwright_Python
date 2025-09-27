# 3. Khai báo biến sau:                                                                                                                                                                                                        
# a = 10                                                                                                                                                                                                        
# b = 3.5                                                                                                                                                                                                        
# c = True                                                                                                                                                                                                        
# d = None                                                                                                                                                                                                        
# e = "Python"                                                                                                                                                                                                 
                                                                                                                                                                                                        
# In ra kiểu dữ liệu của từng biến (type()).                                                                                                                                                                                                        
                                                                                                                                                                                                        
# Tạo list scores = [9, 7, 10, 8, 6] và làm:                                                                                                                                                                                                        
                                                                                                                                                                                                        
# In ra điểm cao nhất.                                                                                                                                                                                                        
                                                                                                                                                                                                        
# Tính điểm trung bình.                                                                                                                                                                                                        
                                                                                                                                                                                                        
# Thêm điểm 5 vào cuối list.                                                                                                                                                                                                        
                                                                                                                                                                                                        
# Tạo tuple birthday = (11, 9, 2025) → in ra ngày, tháng, năm.                                                                                                                                                                                                        
# Thử thay đổi giá trị trong tuple và quan sát lỗi.

a = 10
b = 3.5
c = True
d = None
e = "Python"	

print ("Kiểu dữ liệu của a:", type(a))
print ("Kiểu dữ liệu của b:", type(b))
print ("Kiểu dữ liệu của c:", type(c))
print ("Kiểu dữ liệu của d:", type(d))
print ("Kiểu dữ liệu của e:", type(e))

scores = [9, 7, 10, 8, 6]

print("Điểm cao nhất:", max(scores))
print("Điểm trung bình:", sum(scores)/len(scores))

scores.append(5)
print("list scores sau khi thêm 5:", scores)

birthday = (11, 9, 2025)
print("Ngày", str(birthday[0]) + " Tháng", str(birthday[1]) + " Năm", str(birthday[2]))
# birthday[1] = 10