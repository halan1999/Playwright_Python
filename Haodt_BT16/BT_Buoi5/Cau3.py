# import thư viện để xử lý ngày tháng, thời gian
from datetime import datetime

try:
    #  Nhập dữ liệu
    year_of_birth = int(input("Mời bạn nhập năm sinh nhóe: "))

    # Lấy năm hiện tại
    current_year = datetime.now().year

    # Kiểm tra hợp lệ
    if year_of_birth > current_year:
        raise ValueError("Năm sinh không thể lớn hơn năm hiện tại.")

except ValueError as e:
    # Xử lý lỗi nhập chữ hoặc năm sinh sai
    print("Năm sinh bạn nhập không đúng ròi", e)

else:
    # Năm sinh nhập hợp lệ
    age = current_year - year_of_birth
    print("Tuổi của bạn là:", age)
