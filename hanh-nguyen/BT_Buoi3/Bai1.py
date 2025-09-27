# Khai báo 1 list sản phẩm
products = ["iPhone 13", "Samsung Galaxy", "MacBook Pro 16 inch", "Oppo Reno"]

# Duyệt danh sách và kiểm tra "MacBook Pro 16 inch" có tồn tại không
for find in products:
    if find == "MacBook Pro 16 inch":
        print("Đã tìm thấy sản phẩm")
        break
    else:
        print("Không tìm thấy sản phẩm")