# 1. Tìm kiếm sản phẩm trong list sản phẩm sau
products = ["iPhone 13", "Samsung Galaxy", "MacBook Pro 16 inch", "Oppo Reno"]
print("Lesson 1: Tìm kiếm sản phẩm trong list sản phẩm")
for product in products:
    if product == "MacBook Pro 16 inch":
        print("Đã tìm thấy sản phẩm")
        break

# 2 Nếu không → in "Không tìm thấy sản phẩm".
print("Lesson 2: Tìm kiếm sản phẩm trong list sản phẩm")
products = ["iPhone 13", "Samsung Galaxy", "Oppo Reno"]
for product in products:
    if product == "MacBook Pro 16 inch":
        print("Đã tìm thấy sản phẩm")
    else:
        print("Không tìm thấy sản phẩm")
        break
  
   
