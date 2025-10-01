# for i in range(4):
#     print(i)
# print ("In từ 1 -> 10")
# for i in range(1, 11):
#     print(i)

# print ("In thứ tự số lẻ")
# for i in range(1, 10, 2) :
#     print(i)


# for i in range(1, 21):  # duyệt từ 1 đến 20
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)    

# # Danh sách message mong đợi
# expected_messages = ["Login successful", "Welcome"]

# # Message thực tế
# actual_message = "Welcome"

# # Kiểm tra
# if actual_message in expected_messages:
#     print("Message hop le")
# else:
#     print("Message khong hop le")      


# for i in range(1, 101):  # duyệt từ 1 đến 100
#     if i % 7 == 0:
#         print ("Số đầu tiên từ 1 -> 100 chia hết cho 7 là ", i)
#         break

# scores = [95, 82, 67, 45, 88]

# for score in scores:
#     if score >= 90:
#         rank = "Xuất sắc"
#     elif score >= 70:
#         rank = "Khá"
#     elif score >= 50:
#         rank = "Trung bình"
#     else:
#         rank = "Yếu"
    
#     print("Điểm:", score, "->", rank)

# for i in range(1, 11):
#     print(f"Số tự nhiên: {i}")   
# print("\nBảng cửu chương 2:")
# for i in range(1, 11):
#     print(f"2 x {i} = {2*i}")

# print("\nBảng cửu chương 3:")
# for i in range(1, 11):
#     print(f"3 x {i} = {3*i}")

# print("\nBang cửu chương 4:")
# for i in range(1,11):
#     print(f"4 x {i} = {4*i}")

for num in range(2, 10):   # từ 2 đến 9
    print(f"\nBảng cửu chương {num}:")
    for i in range(1, 11):  # từ 1 đến 10
        print(f"{num} x {i} = {num*i}")


 