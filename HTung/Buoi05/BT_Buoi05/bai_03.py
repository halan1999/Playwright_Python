# Bài 3: File
# Đọc file data.txt.

# Nếu file tồn tại → in nội dung.

# Nếu không → in "File không tồn tại".

# Luôn in "Kết thúc chương trình".

try:
    file = open("dataa.txt","r")
    data = file.read()
    print("Noi dung trong file la:",data)
except FileExistsError as e:
    print("Lỗi tệp tồn tại.",e)
except FileNotFoundError as e:
    print("Lỗi không tìm thấy tệp.",e)
except PermissionError as e:
    print("Không có quyền đọc file.",e)
finally:
    print("Kết thúc chương trình")