scores = [95, 82, 67, 45, 88, 90, 50]

for point in scores:
    if point >= 90:
        rank = "Xuất sắc"
    elif point >= 70:
        rank = "Khá"
    elif point >= 50:
        rank = "Trung bình"
    else:
        rank = "Yếu"
    
    print(f"Điểm {point}: {rank}")
