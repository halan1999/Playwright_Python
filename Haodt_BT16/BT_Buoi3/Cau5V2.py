# San pham trong list có san
products = ["iPhone 13", "Samsung Galaxy", "MacBook Pro 16 inch"]
# Sản phẩm cần check
search_item = "MacBook Pro 16 inch"

# Dùng Flag
flag = False
# Tìm kiếm sản phẩm
for product in products:
    if product == search_item:
        print("Đã tìm thấy sản phẩm")
        flag = True
        break   # thoát vòng lặp khi tìm thấy
# Trả kết quả khi flag=false
if flag==False:
    print("Không tìm thấy sản phẩm")
