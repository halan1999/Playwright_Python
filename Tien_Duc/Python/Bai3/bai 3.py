#bai tap 1
products = ["iPhone 13", "Samsung Galaxy", "MacBook Pro 16 inch", "Oppo Reno"]
product = "MacBook Pro 16 inch"
if product in products:
    print(f'Da tim thay san pham {product} trong danh sach')   
else:
    print(f'Khong tim thay san pham {product}')
#bai tap 2
numbers = [2, 5, 8, 11, 14, 17, 20]
for i in numbers:
    print(i)
    if i%2 == 0:
        print(f'{i} la so chan')
    for a in range(1, 12):
        b = a * i
        print(f"{a},*{i}={b}")