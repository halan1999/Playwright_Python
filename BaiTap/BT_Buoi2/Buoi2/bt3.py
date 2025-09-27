# 3. Khai báo biến sau:                                                                                                                                                                                                                                                                                                                                                  
# a = 10                                                                                                                                                                                                        
# b = 3.5                                                                                                                                                                                                        
# c = True                                                                                                                                                                                                        
# d = None                                                                                                                                                                                                        
# e = ""Python""                                                                                                                                                                                                        
                                                                                                                                                                                                        
# 3.1 In ra kiểu dữ liệu của từng biến (type()).                                                                                                                                                                                                                                                                                                                                                                                                                

# 3.2 Tạo list scores = [9, 7, 10, 8, 6] và làm:                                                                                                                                                              
# 3.2.1 In ra điểm cao nhất.                                                                                                                                                                                                                                                                                                                                                                 
# 3.2.2 Tính điểm trung bình.                                                                                                                                                                                                                                                                                                                                                                                                                
# 3.2.3 Thêm điểm 5 vào cuối list.                                                                                                                                                                                                                                                                                                                                                                                                                

# 3.3 Tạo tuple birthday = (11, 9, 2025) → in ra ngày, tháng, năm.                                                                                                                                                                                                        
# 3.3.1 Thử thay đổi giá trị trong tuple và quan sát lỗi.     

a = 10
b = 3.5
c = True
d = None
e = "Python"

print("Variable type of a:", type(a))
print("Variable type of b:", type(b))
print("Variable type of c:", type(c))
print("Variable type of d:", type(d))
print("Variable type of e:", type(e))
print("\n")

listScores = [9, 7, 10, 8, 6]
highestScore = max(listScores)
averageScore = sum(listScores) / len(listScores) 
print ("Highest score:", highestScore)
print("Average score:", averageScore)

listScores.append(5)
print("Updated list:", listScores)
print("\n")

birthDay = (11, 9, 2025)
print("Day:", birthDay[0])
print("Month:", birthDay[1])
print("Year:", birthDay[2])
print("\n")
# birthDay[0] = 12
# TypeError: 'tuple' object does not support item assignment