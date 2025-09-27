lstNumber = [2, 5, 8, 11, 14, 17, 20]

print("Tất cả số trong list:", lstNumber)

print("Các số chẵn trong list:")
for n in lstNumber:
    if n % 2 == 0:
        print(n)

tong = sum(lstNumber)
print("Tổng các số trong list:", tong)

for n in lstNumber:
    print(f"Bảng cửu chương của {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")