# Tìm kiếm sản phẩm trong list sản phẩm sau
# products = ["iPhone 13", "Samsung Galaxy", "MacBook Pro 16 inch", "Oppo Reno"]
# Viết chương trình duyệt danh sách và kiểm tra xem "MacBook Pro 16 inch" có tồn tại không.
# Nếu có → in "Đã tìm thấy sản phẩm" và dừng vòng lặp (break).
# Nếu không → in "Không tìm thấy sản phẩm"

products = ["iPhone 13", "Samsung Galaxy", "MacBook Pro 16 inch", "Oppo Reno"]
# khởi tạo biến trạng thái

status = False

# thực hiện duyệt danh sách và kiểm trả trạng thái
for search in products :
    if search == "MacBook Pro 16 inchf":
        status =True
        break
if status :
    print("Đã tìm thấy sản phẩm")
else:
    print("Không tìm thấy sản phẩm")