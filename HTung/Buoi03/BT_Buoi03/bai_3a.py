#Phân loại học lực theo điểm trong list sau:                
#scores =[95, 82, 67, 45, 88, 90, 50]
#Từ 90 điểm trở lên -> xuất sắc
# => 70: Khá
#=> 50: trung bình                
# < 50 :Yếu

scores = [95, 82, 67, 45, 88, 90, 50]
for number in scores:
    if number >= 90 :
        print(f"Điểm {number}: Xuất Sắc")
    elif number >= 70:
        print(f"Điểm {number}: Khá")
    elif number >= 50:
        print(f"Điểm {number}: Trung bình")
    else :
        print(f"Điểm {number}: Yếu")
