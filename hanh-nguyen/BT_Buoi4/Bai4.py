# Cho chuỗi sđt: messy_phone = " 090-123 4567 "
messy_phone = " 090-123 4567 "

# Dùng strip() loại bỏ khoảng trắng
print("SĐT sau khi dùng strip() để loại bỏ khoảng trắng:" , messy_phone.strip())

# Dùng replace() để bỏ dấu - và khoảng trắng
print("SĐT sau khi dùng replace() để loại bỏ dấu - và khoảng trắng:" , messy_phone.replace("-" , "").replace(" " , ""))

# In ra SĐT chuẩn hóa: 0901234567
print("SĐT chuẩn hóa:" , messy_phone.replace("-" , "").replace(" " , ""))
