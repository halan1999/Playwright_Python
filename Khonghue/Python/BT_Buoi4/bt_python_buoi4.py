#1 Len() đếm khoảng trắng
text = " hello world "
length_spaces = len(text)
print("Do dai ban dau:", length_spaces)
# strip()
text_strip = text.strip()
length_strip = len(text_strip)
print("Do dai sau:", length_strip)
#2
#In ra chữ hoa
name = "ten ban"
print(name.upper())
#In ra chữ thường toàn bộ
name1 = "TEN BAN"
print(name1.lower())
#In dạng capitalize
print(name.capitalize())
#In dạng title
print(name.title())
#3
s = "Automation Testing"
#Lấy từ " Automation"
print("In tu Automation:",s[0:10])
#Lấy từ "Testting"
print("In tu Testing:",s[11: 18])
#Lấy 5 kí tự đầu
print("In 5 ki tu dau:",s[0:5])
#lấy 3 kí tự cuối
print("In 3 ki tu cuoi:",s[-3:])
#4.
messy_phone = " 090-123 4567 "
#Dung strip
print(messy_phone.strip())
#Dung replace
so = messy_phone.replace("-","")
dt = so.replace(" ", "")
print("So dien thoai can in:", dt)
#Số chuẩn hóa
phone = messy_phone.replace("-", "").replace(" ", "")
print("So dien thoai in:", phone)
#5
fruits = ["apple", "banana", "cherry"]
chuoi = ",".join(fruits)
print("Chuoi tao thanh:", chuoi)
#6
#Kiểm tra ERROR
log = "ERROR: Login failed at 10:45"
check = "ERROR"
if check in log:
    print(" Co loi xay ra")
else:
    print(" He thong binh thuong")  



