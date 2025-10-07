# Xử lý ValueError và lỗi logic với raise
# Bài toán: Viết một chương trình yêu cầu người dùng nhập vào năm sinh và tính tuổi của họ. Chương trình phải xử lý được các trường hợp nhập sai.

# Yêu cầu:
# Sử dụng khối try-except để bắt lỗi ValueError nếu người dùng nhập vào chữ thay vì số.
# Sau khi chuyển đổi thành số thành công, hãy kiểm tra xem năm sinh có hợp lệ hay không (ví dụ: không được lớn hơn năm hiện tại).
# Nếu năm sinh không hợp lệ, hãy dùng raise ValueError để chủ động tạo ra một lỗi với thông báo "Năm sinh không thể lớn hơn năm hiện tại."
# Sử dụng khối else để in ra tuổi của người dùng chỉ khi mọi thứ đều hợp lệ.
from datetime import datetime
current_year = datetime.now().year
try:
    birth_year = int(input("Vui long nhap nam sinh cua ban: "))
    if birth_year > current_year:
        raise ValueError("Nam sinh khong the lon hon nam hien tai.")
except ValueError as e:
    print("Loi:", e)
else:
    age = current_year - birth_year
    print("Tuoi cua ban la:", age)
