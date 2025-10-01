# 1. Tìm kiếm sản phẩm trong list sản phẩm sau
# products = [""iPhone 13"", ""Samsung Galaxy"", ""MacBook Pro 16 inch"", ""Oppo Reno""]

# Viết chương trình duyệt danh sách và kiểm tra xem ""MacBook Pro 16 inch"" có tồn tại không.

# Nếu có → in ""Đã tìm thấy sản phẩm"" và dừng vòng lặp (break).

# Nếu không → in ""Không tìm thấy sản phẩm

products = ["iPhone 13", "Samsung Galaxy", "MacBook Pro 16 inch", "Oppo Reno"]
flag = False
for item in products:
    if item == "MacBook Pro 16 inch":
        flag = True
        break
if flag:
    print("Đã tìm thấy sản phẩm")
else:
    print("Không tìm thấy sản phẩm")

    