
# Bài tập 3: Xử lý ValueError và lỗi logic với raise
# Bài toán: Viết một chương trình yêu cầu người dùng nhập vào năm sinh và tính tuổi của họ. Chương trình phải xử lý được các trường hợp nhập sai.

# Yêu cầu:
# Sử dụng khối try-except để bắt lỗi ValueError nếu người dùng nhập vào chữ thay vì số.
# Sau khi chuyển đổi thành số thành công, hãy kiểm tra xem năm sinh có hợp lệ hay không (ví dụ: không được lớn hơn năm hiện tại).
# Nếu năm sinh không hợp lệ, hãy dùng raise ValueError để chủ động tạo ra một lỗi với thông báo "Năm sinh không thể lớn hơn năm hiện tại."
# Sử dụng khối else để in ra tuổi của người dùng chỉ khi mọi thứ đều hợp lệ.

from datetime import datetime

try:
    
    nam_sinh = int(input("Nhập năm sinh của bạn:"))
    nam_hien_tai = datetime.now().year

    if nam_sinh > nam_hien_tai:
        raise ValueError("Năm sinh không được lớn hơn năm hiện tại")
    if nam_sinh <=0:
        print("Năm sinh là số nguyên dương.")
except ValueError as e:
    print("Lỗi từ hệ thống:",e)
else:
    tuoi = nam_hien_tai - nam_sinh
    print("Tuổi hiện tại của bạn là: ",tuoi)
    