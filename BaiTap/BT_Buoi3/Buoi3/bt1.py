# 1. Tìm kiếm sản phẩm trong list sản phẩm sau
# products = ["iPhone 13", "Samsung Galaxy", "MacBook Pro 16 inch", "Oppo Reno"]
# Viết chương trình duyệt danh sách và kiểm tra xem "MacBook Pro 16 inch" có tồn tại không.
# Nếu có → in "Đã tìm thấy sản phẩm" và dừng vòng lặp (break).
# Nếu không → in "Không tìm thấy sản phẩm".

products = ["iPhone 13", "Samsung Galaxy", "MacBook Pro 16 inch", "Oppo Reno"]
keyWord = "MacBook Pro 16 inch"

for product in products:
    if product == keyWord:
        print("Da tim thay san pham")
        break
else:
    print("Khong tim thay san pham")
