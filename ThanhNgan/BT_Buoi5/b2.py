# "Bài 2: File
# Đọc file data.txt.

# Nếu file tồn tại → in nội dung.

# Nếu không → in ""File không tồn tại"".

# Luôn in ""Kết thúc chương trình""."


try:
    file = open(file = "./data.txt", mode="r", encoding="utf-8")
    content = file.read()
    print("Nội dung file:\n", content)
except (FileNotFoundError, FileExistsError, PermissionError) as e:
    print("File không tồn tại" , e)
finally:
    print("Kết thúc chương trình")
