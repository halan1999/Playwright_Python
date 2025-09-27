from datetime import datetime


try:
    myYear = int(input("Nhập năm sinh của bạn: "))
    yearCurrent = datetime.now().year
    if myYear > yearCurrent:
        raise ValueError("Năm sinh không thể lớn hơn năm hiện tại")

except ValueError as e:
    print(f"Lỗi: {e}")

else:
    print(f"Tuổi: {yearCurrent - myYear}")