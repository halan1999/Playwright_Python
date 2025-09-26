# Tính toán an toàn: Viết chương trình chia 2 số a và b do người dùng nhập. Dùng try-except riêng biệt để bắt lỗi ValueError (nếu nhập chữ) và ZeroDivisionError (nếu chia cho 0) với các thông báo lỗi tương ứng
try:
    a = float(input("Nhập số a: "))
    b = float(input("Nhập số b: "))
    result = a / b
    print(f"Kết quả: {result}")
# except ValueError:
#     print("Lỗi: Vui lòng nhập số hợp lệ.")
# except ZeroDivisionError:
#     print("Lỗi: Không thể chia cho 0.")
    # Tính toán an toàn: Viết chương trình chia 2 số a và b do người dùng nhập. Dùng try-except chung để bắt lỗi ValueError (nếu nhập chữ) và ZeroDivisionError (nếu chia cho 0) với các thông báo lỗi tương ứng
except (ValueError, ZeroDivisionError) as ec:
    print(f"Lỗi: {ec}")