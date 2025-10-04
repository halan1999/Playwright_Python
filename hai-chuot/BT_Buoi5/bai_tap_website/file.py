# NOTE Bài 3: File
# Đọc file data.txt.
# Nếu file tồn tại → in nội dung.
# Nếu không → in "File không tồn tại".
# Luôn in "Kết thúc chương trình".

try:
    file = open("data.txt", "r")
    data = file.read()
    print(data)
except (FileExistsError, FileNotFoundError) as e:
    print(f"Lỗi về file: {e}")
finally:
    print("KẾT THÚC CHƯƠNG TRÌNH!")