# Tạo set email và in
emails_set = {"a@gmail.com", "b@gmail.com", "a@gmail.com"}
print(emails_set)

# Thêm "c@gmail.com"
emails_set.add("c@gmail.com")
print(emails_set)

# Xóa "d@gmail.com" bằng 2 cách và giải thích sự khác nhau
emails_set.remove("d@gmail.com")
emails_set.discard("d@gmail.com")
# Xóa bằng remove sẽ báo lỗi email "d@gmail.com" vì email này không có trong set bên trên
# Xóa bằng discard sẽ không báo lỗi email không có trong set