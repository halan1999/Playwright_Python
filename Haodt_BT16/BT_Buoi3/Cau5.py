# San pham trong list có san
products = ["iPhone 13", "Samsung Galaxy", "MacBook Pro 16 inch", "Oppo Reno"]
# Sản phẩm cần check
search_item = "MacBook Pro 16 inch1"
# Tìm kiếm sản phẩm
for product in products:
    if product == search_item:
        print("Đã tìm thấy sản phẩm")
        break
else:
    print("Không tìm thấy sản phẩm")
