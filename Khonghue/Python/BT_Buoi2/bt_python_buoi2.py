#1. Tính tổng
A = [2, 4, 6, 8, 3, 5]
print (sum(A))
#2.In phan tư Dict
Student = {"name":"Lan", "age":"25", "city": "Ha Noi"}
print(dict(Student))
#3
#Khai bao
a = 10
b = 3.5
c = True
d = None
e = "Python"
#in kieu du lieu
print(type(a),type(b),type(c), type(d), type(e))
#Tao list 
Diem = [9, 7, 10, 8, 6]
print("Diem cao nhat :", max(Diem))
print("Diem trung binh", sum(Diem)/ len(Diem))
#Them diem
Diem.append(5)
print(Diem)
#Tuple birthday
dob = (11, 9, 2025)
print (dob)
#chay loi
#print(dob[6])
#4. Tao dictionary
Student1 = {"name": "Lan", "age": 18, "email":"lan@gmail.com"}
print(Student1["name"])
print(Student1["email"])
#5.Tao set
emails = {"a@gmail.com", "b@gmail.com", "a@gmail.com"}
print(emails)
#them
emails.add("c@gmai.com")
print(emails)
#Xoa
emails.remove("d@gmail.com")
print(emails)
emails.discard("d@gmail.com")
print(emails)
# xóa với remove với mail không có trong list sẽ có thông báo lỗi không có mail xóa được xác định
# xóa với discard với mail không có trong list không có thông báo lỗi và trả kết quả bình thường