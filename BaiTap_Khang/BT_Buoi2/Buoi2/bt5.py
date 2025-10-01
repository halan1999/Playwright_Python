# 5. Tạo set emails = {"a@gmail.com", "b@gmail.com", "a@gmail.com"}
# Quan sát kết quả khi in set ra.
# Thêm "c@gmail.com".
# Thử xóa "d@gmail.com" bằng remove và bằng discard, giải thích sự. khác nhau.

emails = {"a@gmail.com", "b@gmail.com", "d@gmail.com"}
print("Email list:", emails)
emails.add("c@gmail.com")
print("Update email list:", emails)
emails.remove("d@gmail.com") # Nếu phần tử không tồn tại, vd: e@gmail.com thì sẽ báo lỗi
emails.discard("e@gmail.com") # Nếu phần tử không tồn tại, sẽ không báo lỗi