# 2. Cho list số sau
# numbers = [2, 5, 8, 11, 14, 17, 20]
# In ra tất cả số trong list.
# In ra số chẵn trong list.
# Tính tổng tất cả số trong list.
# In ra bảng cửu chương của từng số trong list (gợi ý: dùng for i in range(1, 11):) (bài tập nâng cao dùng for trong for, có thể làm hoặc không)


numbers = [2, 5, 8, 11, 14, 17, 20]
print("Cac so trong list:", *numbers, "\n")

print("Cac so chan tim duoc:")
for number in numbers:
    if number % 2 == 0:
        print(number)
        
print("\nTong cac so trong list:")
sumNumbers = sum(numbers)
print(sumNumbers, "\n")

print("Bang cuu chuong cua tung so:")
for number in numbers:
    print(f"Bang cuu chuong {number}:")
    for i in range(1,11):
        mutipleNumbers = number * i
        print(f"{number} * {i} = {mutipleNumbers}")
    print("------------")