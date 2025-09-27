try:
    # Mở và đọc file
    with open("../python/BT_Buoi5/data.txt", "r", encoding="utf-8") as f:
        datatest = f.read()
        print("Nội dung file:")
        print(datatest)

except FileNotFoundError:
    # Nếu file không tồn tại
    print("File không tồn tại")

finally:
    # Luôn chạy dù có lỗi hay không
    print("Kết thúc chương trình")
