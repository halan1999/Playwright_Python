#bai tap 1: Kiểm trả message đăng nhập xem có nằm trong danh sách sau:
#expected_messages = [“Login succesfull”, “Welcome”]      
#actual_message = “Welcome”                    
#Nếu actual message nằm trong expected_messages thì in ra “Message valid” ngược lại thì in ra “Message invalid”
expected_message = ["login successfull", "welcome"]
actual_message = "welcome"
if actual_message in expected_message:
    print("Message valid")
else:
    print("Message invalid")

#Bai tập 2: Tìm số chia hết cho 7 đầu tiên trong dãy từ 1 đến 100 và in ra màn hình
for i in range(1, 100):
    if i % 7 == 0:
        print("số chia hết cho 7 đầu tiên là", i)
        break

#Bài tập 3: Phân loại học lực theo điểm trong list sau:                
#scores =[95, 82, 67, 45, 88, 90, 50]
#Từ 90 điểm trở lên -> xuất sắc
# => 70: Khá
#=> 50: trung bình                
#< 50 :Yếu
scores = [95, 82, 67, 45, 88, 90, 50]
excellent = 0
good = 0
average = 0
weak = 0
for x in scores:
    if x >= 90:
        excellent +=1
    elif x >= 70:
        good += 1
    elif x >= 50:
        average += 1
    else:
        weak += 1
print("có", excellent, "học sinh xuất sắc")
print("có", good,"học sinh khá")
print("có", average,"học sinh trung bình")
print("có", weak,"học sinh yếu")

#Bài tập 4: in ra bản cửu chương 2 và 3
#Bảng cửu chương 2
print("Bảng cửu chương 2")
for i in range(1, 11):
    print("2 x",i,"=",2 * i)
print("Bảng cửu chương 3")
for x in range(1, 11):
    print("3 x",x,"=",3 * x)

#Bài Tập 5: Tìm kiếm sản phẩm trong list sản phẩm sau
#products = ["iPhone 13", "Samsung Galaxy", "MacBook Pro 16 inch", "Oppo Reno"]
#Viết chương trình duyệt danh sách và kiểm tra xem "MacBook Pro 16 inch" có tồn tại không.
#Nếu có → in "Đã tìm thấy sản phẩm" và dừng vòng lặp (break).
#Nếu không → in "Không tìm thấy sản phẩm".
products = ["iPhone 13", "Samsung Galaxy", "MacBook Pro 16 inch", "Oppo Reno"]
for i in products:
 if i == "MacBook Pro 16 inch":
  print("Đã tìm thấy sản phẩm")
  break
 else:
  print("Không tìm thấy sản phẩm")

#Bài tập 6: Cho list số sau
#numbers = [2, 5, 8, 11, 14, 17, 20]
#In ra tất cả số trong list.
#In ra số chẵn trong list.
#Tính tổng tất cả số trong list.
#In ra bảng cửu chương của từng số trong list (gợi ý: dùng for i in range(1, 11)

numbers = [2, 5, 8, 11, 14, 17, 20]
#In ra tất cả số trong list.
for x in numbers:
 print("các số trong list numbers là:", x)
#In ra số chẵn trong list.
for i in numbers:
 if i % 2 == 0:
  print("số chẵn là", i)
#Tính tổng tất cả số trong list.
y = sum(numbers)
print("tong tat ca so trong list la", y)
#In ra bảng cửu chương của từng số trong list (gợi ý: dùng for i in range(1, 11)
for z in numbers:
 for d in range(1, 11):
  cuu_chuong = z * d
  print("bang cuu chuong cua",z,"la",z,"*",d,"=", cuu_chuong)