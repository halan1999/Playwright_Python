# NOTE 2: Tìm số chia hết cho 7 đầu tiên trong dãy từ 1 đến 100 và in ra màn hình
for number in range(1,100):
    if number % 7 == 0:
        print(f"Số đầu tiên chia hết cho 7: {number}")
        break