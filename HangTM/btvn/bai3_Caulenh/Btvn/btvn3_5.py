# products = ["iPhone 13", "Samsung Galaxy", "MacBook Pro 16 inch", "Oppo Reno"]
# if "macbook pro 16 inch" in products:
#     print("đã tìm thấy sản phẩm")
# else:
#     print("không tìm thấy sản phẩm")

products = ["iPhone 13", "Samsung Galaxy", "MacBook Pro 16 inch", "Oppo Reno"]
flag=False
for product in products:
    if (product=="MacBook Pro 16 inch"):
        flag=True
        print("đã tìm thấy sản phẩm")
        break
if not flag:
    print("không tìm thấy sản phẩm")