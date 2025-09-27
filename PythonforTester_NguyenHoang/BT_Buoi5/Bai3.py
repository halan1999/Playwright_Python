# Bài toán: Viết một chương trình yêu cầu người dùng nhập vào năm sinh và tính tuổi của họ. Chương trình phải xử lý được các trường hợp nhập sai.

# Yêu cầu:
# Sử dụng khối try-except để bắt lỗi ValueError nếu người dùng nhập vào chữ thay vì số.
# Sau khi chuyển đổi thành số thành công, hãy kiểm tra xem năm sinh có hợp lệ hay không (ví dụ: không được lớn hơn năm hiện tại).
# Nếu năm sinh không hợp lệ, hãy dùng raise ValueError để chủ động tạo ra một lỗi với thông báo ""Năm sinh không thể lớn hơn năm hiện tại.""
# Sử dụng khối else để in ra tuổi của người dùng chỉ khi mọi thứ đều hợp lệ."

try:
    namsinh = int(input("Hãy cho biết năm sinh của bạn: "))
    if namsinh > 2025:
        raise ValueError("Năm sinh không thể lớn hơn năm hiện tại")
except ValueError as e:
    print("Lỗi dữ liệu:", e)
else:
    print("Tuổi bạn là:", 2025 - namsinh)