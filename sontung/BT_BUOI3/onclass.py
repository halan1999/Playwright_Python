# for i in range(1, 21):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

# ------------------------------------- #
expected_messages = ["Login successfully", "Welcome"]
actual_message = "Welcome"

if actual_message in expected_messages:
    print("Message hop le")
else:
    print("Message ko hop le")

# --------------------------------------- #
for i in range(1, 101):
    if i % 7 == 0:
        print("Số chia hết cho 7 đầu tiên:", i)
        break

# --------------------------------------- #
lstScores = [95, 82, 67, 45, 88, 90, 50]

for score in lstScores:
    if score >= 90:
        print(score, ": Xuất sắc")
    elif score >= 70:
        print(score, ": Khá")
    elif score >= 50:
        print(score, ": Trung bình")
    else:
        print(score, ": Yếu")

# ---------------------------------------- #
print("Bảng cửu chương 2:")
for i in range(1, 11):
    print(f"2 x {i} = {2 * i}")

print("\nBảng cửu chương 3:")
for i in range(1, 11):
    print(f"3 x {i} = {3 * i}")
