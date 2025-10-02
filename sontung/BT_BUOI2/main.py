# Bai 1
lstNum = [1, 2, 3, 4, 5]
total = sum(lstNum)

print("Tổng: ", total)

# Bai 2
dictInfo = {"name":"Lan", "age":18, "city":"Hanoi"}
print(dictInfo)

# Bai 3
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

#--------------------------------------#
lstScores = [9, 7, 10, 8, 6]

print("Điểm cao nhất:", max(lstScores))

avg = sum(lstScores) / len(lstScores)
print("Điểm trung bình:", avg)

lstScores.append(5)
print("Danh sách sau khi thêm điểm 5 vào cuối list:", lstScores)

#--------------------------------------#
birthday = (9, 9, 1995)

print("Ngày:", birthday[0])
print("Tháng:", birthday[1])
print("Năm:", birthday[2])

# Bai 4
dictInfo = {"name":"Tung", "age":18, "email":"test@gmail.com"}
print(dictInfo["name"])
print(dictInfo["age"])
print(dictInfo["email"])

# Bai 5
setEmails = {"a@gmail.com", "b@gmail.com", "a@gmail.com"}
print("Ban đầu:", setEmails)

setEmails.add("c@gmail.com")
print("Sau khi thêm c@gmail.com:", setEmails)

# setEmails.remove("d@gmail.com")

setEmails.discard("d@gmail.com")
print("Sau khi discard:", setEmails)



