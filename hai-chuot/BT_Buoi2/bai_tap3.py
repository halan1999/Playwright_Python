# NOTE BÀI 3: Khai báo biến sau:                                                                                                                                                        
# a = 10                                                                                                                                                                                                        
# b = 3.5                                                                                                                                                                                                        
# c = True                                                                                                                                                                                                        
# d = None                                                                                                                                                                                                        
# e = "Python" 
# In ra kiểu dữ liệu của từng biến (type()). 
a = 10                                                                                                                                                                                                        
b = 3.5                                                                                                                                                                                                        
c = True                                                                                                                                                                                                        
d = None                                                                                                                                                                                                        
e = "Python"
print(f'''KẾT QUẢ BÀI 3:
+ Kiểu dữ liệu của a: {type(a)}
+ Kiểu dữ liệu của b: {type(b)}
+ Kiểu dữ liệu của c: {type(c)}
+ Kiểu dữ liệu của d: {type(d)}
+ Kiểu dữ liệu của e: {type(e)}''')
print()

# Tạo list scores = [9, 7, 10, 8, 6] và làm:                                                                                                                                                            
# In ra điểm cao nhất.                                                                                                                                                                                
# Tính điểm trung bình.                                                                                                                                                                              
# Thêm điểm 5 vào cuối list.                                                                                                                                                                                                        
lst_score = [9, 7, 10, 8, 6]
print(f"Điểm cao nhất: {max(lst_score)}")

average_score = sum(lst_score) / len(lst_score)
print(f"Điểm trung bình: {average_score}")

lst_score.append(5)
print(f"List sau khi thêm phần tử: {lst_score}")
print()

# Tạo tuple birthday = (11, 9, 2025) → in ra ngày, tháng, năm.                                                                                                                                                                                                        
# Thử thay đổi giá trị trong tuple và quan sát lỗi.
my_birthday = (4, 12, 1991)
print(f"Ngày sinh: {my_birthday[0]}")
print(f"Tháng sinh: {my_birthday[1]}")
print(f"Năm sinh: {my_birthday[-1]}")

# Thử thay đổi giá trị trong tuple và quan sát lỗi 
my_birthday[1] = 13