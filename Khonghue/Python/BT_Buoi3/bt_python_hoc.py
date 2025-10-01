#1.Ktra mess login
expected_messages = ["Login succesfull","Welcome"]
actual_message = "Welcome"   
for actual_message in expected_messages:
    if actual_message in expected_messages:
        print("Message valid")
    else :
        print("Message invalid")
#2.So chia het cho 7 dau tien trong day 1-100
    for i in range(1, 101):
        if i % 7 == 0:
            print("So chia het cho 7 dau tien la:", i)
            break
#3.Phan loai hoc luc
scores = [95, 82, 67, 45, 88, 90, 50]
for n in scores:
    if n >= 90:
        print("Hoc sinh xuat xac", n)
    elif n >= 70:
        print("Hoc sinh kha", n)
    elif n >= 50:
        print("Hoc sinh trung binh", n)
    else : 
        print("Hoc luc yeu", n)
#4. In bang cuu chuong 2 
for a in range (1, 11):
    h = 2*a
    # print (f"bang cuu chuong 2 : 2*{a} = {h}") -> mục đích đặt chữ f trước chuỗi và dùng {} bao quanh biến/biểu thức
    # print ("Bang cuu chuong so 2 :", h)
    print ("Bang cuu chuong so 2:", "2 *", a, "=", h)
#4.1. In bang cuu chuong 3
for a in range (1, 11):
    b = 3 * a
    print("Bang cuu chuong so 3:", "3 *", a, "=", b)



