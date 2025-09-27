a = input('nhap so nguyen a')
try:
    a = int(a)
except:
    print('a khong phai la so nguyen')
else:
    print('binh phuong cua so nguyen do la:', a*a)
finally:
    print('cam on ban da su dung chuong trinh')

try:
    file = open('./data.txt', 'r')
    data = file.read()
    print('Noi dung trong file la:', data)
except (FileNotFoundError, FileExistsError, PermissionError) as e:
    print('Loi, ly do:', e)

#"Bài tập 3: Xử lý ValueError và lỗi logic với raise
#Bài toán: Viết một chương trình yêu cầu người dùng nhập vào năm sinh và tính tuổi của họ. Chương trình phải xử lý được các trường hợp nhập sai.

#Yêu cầu:
#Sử dụng khối try-except để bắt lỗi ValueError nếu người dùng nhập vào chữ thay vì số.
#Sau khi chuyển đổi thành số thành công, hãy kiểm tra xem năm sinh có hợp lệ hay không (ví dụ: không được lớn hơn năm hiện tại).
#Nếu năm sinh không hợp lệ, hãy dùng raise ValueError để chủ động tạo ra một lỗi với thông báo ""Năm sinh không thể lớn hơn năm hiện tại.""
#Sử dụng khối else để in ra tuổi của người dùng chỉ khi mọi thứ đều hợp lệ."

Year = input('Nhap nam sinh cua ban: ')
try:
    year = int(Year)
    if year > 2025:
        raise ValueError('Nam sinh khong the lon hon nam hien tai.')
except ValueError as e:
    print('Loi, ly do:', e)
else: 
    age = 2025 - year
    print('Tuoi cua ban la:', age)
finally:
    print('Cam on ban da su dung chuong trinh')
