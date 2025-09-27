# 5. Tạo set emails = {""a@gmail.com"", ""b@gmail.com"", ""a@gmail.com""}.
# Quan sát kết quả khi in set ra.
# Thêm ""c@gmail.com"".
# Thử xóa ""d@gmail.com"" bằng remove và bằng discard, giải thích sự khác nhau."

emails = {"a@gmail.com", "b@gmail.com", "a@gmail.com"}
print(emails) 
# Chỉ in ra 2 phần tử là "a@gmail.com" và "b@gmail.com"

# Thêm "c@gmail.com"
emails.add("c@gmail.com") 

# Xóa "d@gmail.com"  bằng remove -> báo Eror do trong set emails không có phần tử "d@gmail.com"
# emails.remove("d@gmail.com")

# Xóa "d@gmail.com" bằng discard -> không báo lỗi
# emails.discard("d@gmail.com")