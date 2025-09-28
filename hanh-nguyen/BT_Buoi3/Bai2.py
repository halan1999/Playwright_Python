# Khai báo list số
numbers = [2, 5, 8, 11, 14, 17, 20]

# In ra tất cả các số trong list
print("Các số có trong list gồm " , numbers)

# In ra sỗ chẵn trong list
for c in numbers:
    if c % 2 == 0:
        print(f"Số {c} là số chẵn trong list")

# Tính tổng tất cả các số trong list
print("Tổng các số có trong list là:" , sum(numbers))

# In bảng cửu chương của từng số trong list
for m in numbers:
    print(f"Bảng cửu chương của {m} là")
    for i in range (1, 11):
        print(f"{m} x {i} = {m*i}")