#Bai 1: list va tinh tong list
test1 = [1,5,8,4,8]
print (sum(test1))

#Bai 2: dictionary va in ra gia tri cua dict
test2 = {"name": "Lan","age": 25,"city": "Ha Noi"}
print (test2["name"],test2["age"],test2["city"])

#Ba 3
#khai bao bien va check xem loai bien
a = 10
b = 3.5
c = True
d = None
e = "Python"
print(type(a),type(b),type(c),type(d),type(e)) #<class 'int'> <class 'float'> <class 'bool'> <class 'NoneType'> <class 'str'>

#tao list va tinh diem cao nhat, diem trung binh, them diem 5 vao cuoi list
scores = [9, 7, 10, 8, 6]
# tinh diem cao nhat
print(max(scores)) #điểm cao nhất là 10
# tinh diem trung binh
avarge = sum(scores) / len(scores)
print(avarge) #điểm trung bình sẽ là 8.0
# thêm giá trị 5 vào cuối list
scores.append(5) #giá trị 5 được thêm vào cuối list
print(scores)
scores.insert(5, 5) #giá trị 5 được thêm vào vị trí cuối cùng của list
print(scores)
# tao tuple
birthday = (11,9,2025)
#birthday[0] = 12 # the system return 'tuple' object does not support item assignment
print(birthday)

#Bai 4: tao Dictionary va in ra ten va email
student = {"name":"Lan", "age":18, "email":"lan@gmail.com"}
print(student["name"],student["email"])

#Bai 5: Tạo set
emails = {"a@gmail.com","b@gmail.com","a@gmail.com"}
print(emails) #giá trị a@gmail.com chỉ in ra 1 giá trị và giá trị của set emails sẽ random
#thêm c@gmail.com
emails.add("c@gmail.com")
print(emails) #giá trị c@gmail.com được thêm vào set emails