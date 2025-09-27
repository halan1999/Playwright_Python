# NOTE BÀI 5: Tạo set emails = {"a@gmail.com", "b@gmail.com", "a@gmail.com"}
# Quan sát kết quả khi in set ra
print("KẾT QUẢ BÀI 5: ")
set_email = {"a@gmail.com", "b@gmail.com", "a@gmail.com"}
print(set_email)

# Thêm "c@gmail.com"
set_email.add("c@gmail.com")
print(set_email)

# Thử xóa "d@gmail.com" bằng remove và bằng discard, giải thích sự khác nhau
set_email.discard("d@gmail.com") # Không thông báo lỗi
set_email.remove("d@gmail.com") # Báo lỗi do không có phần tử này trong set