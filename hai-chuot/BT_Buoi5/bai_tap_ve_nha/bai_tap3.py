# NOTE Bài 3: Xử lý ValueError và lỗi logic với raise
# Bài toán: Viết một chương trình yêu cầu người dùng nhập vào năm sinh và tính tuổi của họ. Chương trình phải xử lý được các trường hợp nhập sai.

# Yêu cầu:
# Sử dụng khối try-except để bắt lỗi ValueError nếu người dùng nhập vào chữ thay vì số.
# Sau khi chuyển đổi thành số thành công, hãy kiểm tra xem năm sinh có hợp lệ hay không (ví dụ: không được lớn hơn năm hiện tại).
# Nếu năm sinh không hợp lệ, hãy dùng raise ValueError để chủ động tạo ra một lỗi với thông báo "Năm sinh không thể lớn hơn năm hiện tại."
# Sử dụng khối else để in ra tuổi của người dùng chỉ khi mọi thứ đều hợp lệ.

from datetime import date

def cal_age(year_of_birth):
    current_date = date.today()
    current_year = current_date.year
    result = current_year - year_of_birth
    if result <= 0:
        raise ValueError("Năm sinh không thể lớn hơn năm hiện tại")
    else:
        return result

try:
    nam_sinh = int(input("Xin mời nhập năm sinh của bạn: "))
    tuoi = cal_age(nam_sinh)
except ValueError as e:
    print(e)
else:
    print(f"Tuổi của bạn: {tuoi}")
finally:
    print("KÊT THÚC CHƯƠNG TRÌNH!")