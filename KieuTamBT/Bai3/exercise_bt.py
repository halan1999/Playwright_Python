# products = ["iPhone 13", "Samsung Galaxy", "MacBook Pro 16 inch", "Oppo Reno"]
# found = False
# for p in products:
#     if(p == "MacBook Pro 17 inch"):
#         print("Đã tìm thấy sản phẩm")
#         found = True
#         break
# if not found:
#     print("Không tìm thấy sản phẩm")

numbers = [2, 5, 8, 11, 14, 17, 20]
for n in numbers:
    print(n, end=" ")

print("\n")

print("In các số chẵn: ")
for n in numbers:
    if(n%2 == 0):
        print(n, end=" ")