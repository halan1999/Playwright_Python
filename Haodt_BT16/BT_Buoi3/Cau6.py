numbers = [2, 5, 8, 11, 14, 17, 20]

# 1. In ra tất cả số trong list
# end là in khoảng trắng, trên cùng 1 dòng 
print("Tất cả các số trong list:")
for number in numbers:
    print(number, end=' ')
print("\n")  # xuống dòng

# 2. In ra số chẵn trong list
print("Các số chẵn trong list:")
for number in numbers:
    if number % 2 == 0:
        print(number, end=' ')
print("\n")

# 3. Tính tổng tất cả số trong list
total = sum(numbers)
print(f"Tổng tất cả các số trong list: {total}\n")

# 4. In ra bảng cửu chương của từng số trong list
for number in numbers:
    print(f"Bảng cửu chương của {number}:")
    for i in range(1, 11):
        print(f"{number} x {i} = {number*i}")
    print()  # xuống dòng giữa các bảng
