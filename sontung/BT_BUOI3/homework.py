# Bài 1
lstProducts = ["IPhone 17 Pro Max", "Samsung Galaxy S25 Ultra", "MacBook Pro 16 inch", "Oppo Reno 14"]

for p in lstProducts:
    if p == "MacBook Pro 16 inch":
        print("Đã tìm thấy sản phẩm")
        break
else:
    print("Không tìm thấy sản phẩm")

# Bài 2
lstNumber = [2, 5, 8, 11, 14, 17, 20]

print("\nTất cả số trong list:", *lstNumber)

print("\nCác số chẵn trong list:")
for n in lstNumber:
    if n % 2 == 0:
        print(n)

tong = sum(lstNumber)
print("\nTổng các số trong list:", tong)

for n in lstNumber:
    print(f"\nBảng cửu chương của {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

