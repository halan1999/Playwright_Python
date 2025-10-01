# 1. Tạo list gồm 5 số, tính tổng tất cả các số trong list.
list_5_numbers = [1, 3, 5, 7, 10]
sumtList = sum(list_5_numbers)
print("Total:", sumtList)
print("\n")

# 2. Viết chương trình in ra tất cả các phần tử của dict {"name": "Lan", "age": 25, "city": "Hà Nội"}.
employeeInformation = {
    "name": "Lan",
    "age": 25,
    "city": "Ha Noi"
}
print("Name:", employeeInformation["name"])
print("Age:", employeeInformation["age"])
print("City:", employeeInformation["city"])
print("\n")

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

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
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

# 4. Tạo dictionary student = {"name": "Lan", "age": 18, "email": "lan@gmail.com"}
# In ra tên và email.
studentInformation = {
    "name": "Lan",
    "age": 18,
    "email": "lan@gmail.com"
}
print("Name:", studentInformation["name"])
print("Email:", studentInformation["email"])
print("\n")

# 5. Tạo set emails = {"a@gmail.com", "b@gmail.com", "a@gmail.com"}
# Quan sát kết quả khi in set ra.
# Thêm "c@gmail.com".
# Thử xóa "d@gmail.com" bằng remove và bằng discard, giải thích sự. khác nhau.

emails = {"a@gmail.com", "b@gmail.com", "d@gmail.com"}
print("Email list:", emails)
emails.add("c@gmail.com")
print("Update email list:", emails)
emails.remove("d@gmail.com") # Nếu phần tử không tồn tại, vd: e@gmail.com thì sẽ báo lỗi
emails.discard("e@gmail.com") # Nếu phần tử không tồn tại, sẽ không báo lỗi
