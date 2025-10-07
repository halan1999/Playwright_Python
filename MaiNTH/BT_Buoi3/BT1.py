#1. Kiểm trả message đăng nhập xem có nằm trong danh sách sau không:
 
expected_messages = ["Login succesfull", "Welcome"]
actual_message = "Welcome"
# Nếu actual message nằm trong expected_messages thì in ra “Message valid” ngược lại thì in ra “Message invalid”
print("Lesson 1: Kiểm tra message đăng nhập")
if actual_message in expected_messages:
    print("Message valid")

# 2.Tìm số chia hết cho 7 đầu tiên trong dãy từ 1 đến 100 và in ra màn hình
print("Lesson 2: Tìm số chia hết cho 7 đầu tiên trong dãy từ 1 đến 100")
for number in range(1, 101):
    if number % 7 == 0:
        print(f"Số chia hết cho 7 đầu tiên trong dãy từ 1 đến 100 là: {number}")
        break

# 3.Phân loại học lực theo điểm trong list sau:                 
# scores =[95, 82, 67, 45, 88, 90, 50]
# Từ 90 điểm trở lên -> xuất sắc
#  => 70: Khá
# => 50: trung bình                 
# < 50 :Yếu
scores = [95, 82, 67, 45, 88, 90, 50]
print("Lesson 3: Phân loại học lực theo điểm")
for score in scores:
    if score >= 90:
        print(f"Điểm {score}: Xuất sắc")
    elif score >= 70:
        print(f"Điểm {score}: Khá")
    elif score >= 50:
        print(f"Điểm {score}: Trung bình")
    else:
        print(f"Điểm {score}: Yếu") 


# 4.1 In ra bảng cửu chương 2
print("Lesson 4.1: In ra bảng cửu chương 2")
for i in range(1, 11):
    result = 2 * i
    print(f"2 x {i} = {result}")
# 4.2. In ra bảng của chương 3
print("Lesson 4.2: In ra bảng cửu chương 3")
for i in range(1, 11):
    result = 3 * i
    print(f"3 x {i} = {result}")
