# NOTE 1: Tìm kiếm sản phẩm trong list sản phẩm sau
# products = ["iPhone 13", "Samsung Galaxy", "MacBook Pro 16 inch", "Oppo Reno"]
# Viết chương trình duyệt danh sách và kiểm tra xem "MacBook Pro 16 inch" có tồn tại không.
# Nếu có → in "Đã tìm thấy sản phẩm" và dừng vòng lặp (break).
# Nếu không → in "Không tìm thấy sản phẩm".

# Tạo hàm kiểm tra sản phẩm trong list
def check_product(lst_expected_products, actual_product):
    result_search = False
    for expected_product in lst_expected_products:
        if actual_product == expected_product:
            result_search = True
            break
    
    if result_search == True:
        print(f"Đã tìm thấy sản phẩm {actual_product} trong Danh sách sản phẩm")
    else:
        print(f"Không tìm thấy sản phẩm {actual_product} trong Danh sách sản phẩm")

# Khởi tạo list sản phẩm  
list_products = ["iPhone 13", "Samsung Galaxy", "MacBook Pro 16 inch", "Oppo Reno"]

actual_product1 = "MacBook Pro 16 inch"
actual_product2 = "Lenovo X1 Carbon"

# Kiểm tra từng sản phẩm
check_product(list_products, actual_product1)
print()
check_product(list_products, actual_product2)