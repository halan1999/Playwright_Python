print("**************** Kết quả bài 1 ****************")
print("\nkiểm tra xem MacBook Pro 16 inch có tồn tại không?")
products = ["iPhone 13", "Samsung Galaxy", "MacBook Pro 16 inch", "Oppo Reno"]

found = False
for p in products:
    if p == "MacBook Pro 16 inch":
        print("=> Đã tìm thấy sản phẩm")
        found = True
        break

if not found:
    print("Không tìm thấy sản phẩm")

print("\n**************** Kết quả bài 2 ****************")
numbers = [2, 5, 8, 11, 14, 17, 20]

print("Tất cả số trong list:")
for n in numbers:
    print(n, end=" ")
print("\n")

# In ra số chẵn
print("Các số chẵn trong list:")
for n in numbers:
    if n % 2 == 0:
        print(n, end=" ")
print("\n")

# Tính tổng
total = sum(numbers)
print("Tổng tất cả số trong list:", total)

# Bảng cửu chương cho từng số (for trong for)
print("\n--- Bảng cửu chương cho từng số ---")
for n in numbers:
    print(f"\nBảng cửu chương {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")    