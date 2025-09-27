# File
# Đọc file data.txt
# Nếu file tồn tại → in nội dung.
# Nếu không → in "File không tồn tại".
# Luôn in "Kết thúc chương trình".

try:
    with open("data.txt", "r") as f:
        print(f.read())
except FileNotFoundError as e:
    print("File does not exist!")
finally:
    print("\nEnd program")