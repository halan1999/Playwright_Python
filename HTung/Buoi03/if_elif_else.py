# Khi chúng ta có nhiều điều kiện cần kiểm tra, if-elif-else là công cụ hoàn hảo. elif là viết tắt của "else if". Chương trình sẽ kiểm tra các điều kiện từ trên xuống dưới:
# Kiểm tra if. Nếu đúng, thực thi và kết thúc.
# Nếu if sai, kiểm tra elif đầu tiên. Nếu đúng, thực thi và kết thúc.
# Cứ tiếp tục như vậy cho đến hết các elif.
# Nếu tất cả if và elif đều sai, khối lệnh của else sẽ được thực thi.

#Cú pháp
# if dieu_kien_1:
    # Thực thi nếu dieu_kien_1 là True
# elif dieu_kien_2:
    # Thực thi nếu dieu_kien_1 là False VÀ dieu_kien_2 là True
# else:
    # Thực thi nếu tất cả các điều kiện trên đều False

# e.g
Diem_tb = 6.5

if Diem_tb >= 6.5:
    print("Học lực: Khá")
elif Diem_tb >= 7.5 :
    print ("Học lực: Giỏi")
elif Diem_tb >= 5 :
    print("Học lực: Trung Bình")
else :
    print("Học lực: Yếu")

#-----------------------------------
# kiểm tra các lỗi thường gặp trong test API
 
StatusCode_API = 200

if StatusCode_API == 500:
    print(f"Lỗi {StatusCode_API} phía máy chủ – Máy chủ không thể hoàn thành yêu cầu được cho là hợp lệ.")
elif StatusCode_API == 200:
    print("Phản hồi thành công – Yêu cầu đã được máy chủ tiếp nhận, hiểu và xử lý thành công.")
elif StatusCode_API == 300:
    print("Điều hướng – Phía client cần thực hiện hành động bổ sung để hoàn tất yêu cầu.")
elif StatusCode_API == 400:
    print("Lỗi phía client – Yêu cầu không thể hoàn tất hoặc yêu cầu chứa cú pháp không chính xác.")
else:
    print("Phản hồi thông tin – Yêu cầu đã được chấp nhận và quá trình xử lý yêu cầu đang được tiếp tục.")