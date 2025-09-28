#  2. Cho list số sau
# numbers = [2, 5, 8, 11, 14, 17, 20]
numbers = [2, 5, 8, 11, 14, 17, 20]


# In ra tất cả số trong list.
print("Lesson 1: In ra tất cả số trong list")
for number in numbers:
    print(number)
print()


# In ra số chẵn trong list.
print("Lesson 2: In ra số chẵn trong list")
for number in numbers:
    if number % 2 == 0:
        print(number)
print()

# Tính tổng tất cả số trong list.
print("Lesson 3: Tính tổng tất cả số trong list")
total = sum(numbers)
print(f"Tổng tất cả số trong list là: {total}")
print()


# In ra bảng cửu chương của từng số trong list 
print("Lesson 4: In ra bảng cửu chương của từng số trong list")
for number in numbers:
    print(f"Bảng cửu chương của {number}:")
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")
    print()  # In dòng trống giữa các bảng cửu chương

 	 
    
