# Cấu trúc if-else đưa ra hai lựa chọn: một cho trường hợp điều kiện đúng, và một cho tất cả các trường hợp còn lại (khi điều kiện sai).

age = 10
if age >= 20:
    print("Bạn đã đủ tuổi. Chúc bạn xem phim vui vẻ!")
else :
    print("Hẹn bạn lần sau nhé! Hẹ Hẹ") 

# Kiểm tra một số là chẵn hay lẻ. Một số hoặc là chẵn, hoặc là lẻ, không có trường hợp khác
# Thông thường các số chẵn thường chúng ta chia hết cho 2.

number = 8
if number % 2 == 0:
    print("Số này là số chẵn")
else:
    print("Số này là số lẽ")