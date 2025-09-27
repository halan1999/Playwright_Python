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

#tạo list
lstScores = [9,7,10,8,6]
#điểm trung bình
avgScores = sum(lstScores)/len(lstScores)

#in ra màn hình
print('Điểm cao nhất', max(lstScores))
print('Điểm trung bình' , avgScores)

#thêm phần tử 5 vào cuối list
lstScores.append(5)
print(lstScores)

#birthday
birthday = (11,9,2025)
print('Ngày', birthday[0])
print('Tháng', birthday[1])
print('Năm', birthday[2])