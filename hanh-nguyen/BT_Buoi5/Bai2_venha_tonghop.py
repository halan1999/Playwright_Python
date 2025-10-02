# Đọc file data.txt.
# Nếu file tồn tại → in nội dung.
# Nếu không → in "File không tồn tại".
# Luôn in "Kết thúc chương trình"."

# Trường hợp có tìm thấy file
try:
    f = open("data.txt", "r")
    data = f.read()
except FileNotFoundError:
    print("File không tồn tại")
else:
    print("Nội dung của file data.txt la:\n", data)
finally:
    print("Kết thúc chương trình")

# Trường hợp không tìm thấy file
try:
    f = open("testdata.txt", "r")
    data = f.read()
except FileNotFoundError:
    print("File không tồn tại")
else:
    print("Nội dung của file data.txt la:\n", data)
finally:
    print("Kết thúc chương trình")