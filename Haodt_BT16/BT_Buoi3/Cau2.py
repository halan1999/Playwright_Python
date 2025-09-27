# Tìm số chia hết cho 7 đầu tiên trong dãy từ 1 đến 100
for i in range(1, 101):
    if i % 7 == 0:
        print("Số chia hết cho 7 đầu tiên là:", i)
        break
