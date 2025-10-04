# NOTE 3: Phân loại học lực theo điểm trong list sau:                 
# scores =[95, 82, 67, 45, 88, 90, 50]
# Từ 90 điểm trở lên -> xuất sắc
#  => 70: Khá
# => 50: trung bình                 
# < 50 :Yếu

lst_scores = [95, 82, 67, 45, 88, 90, 50]
for score in lst_scores:
    if score >= 90:
        print(f"Điểm số: {score} --> Đạt loại Xuất sắc")
    elif score >= 70:
        print(f"Điểm số: {score} --> Đạt loại Khá")
    elif score >= 50:
        print(f"Điểm số: {score} --> Đạt loại Trung bình")
    else:
        print(f"Điểm số: {score} --> Đạt loại Yếu")