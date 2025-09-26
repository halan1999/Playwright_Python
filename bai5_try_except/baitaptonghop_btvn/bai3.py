# Đọc file data.txt.

# Nếu file tồn tại → in nội dung.

# Nếu không → in "File không tồn tại".

# Luôn in "Kết thúc chương trình".
try:
    with open("data.txt", "r", encoding="utf-8") as file:
        data = file.read()
    # file=open("data.txt","r",encoding="utf-8")
    #  data=file.read()
    print("nội dung file là:",data)
except FileNotFoundError:
    print("File không tồn tại")
finally:
    print("Kết thúc chương trình")