# 4. Cho chuỗi số điện thoại:
# messy_phone = " 090-123 4567 "
 
# Dùng strip() để bỏ khoảng trắng.
# Dùng replace() để bỏ dấu - và khoảng trắng.
# In ra số điện thoại chuẩn hóa: 0901234567.

# Tạo chuỗi
messy_phone = " 090-123 4567 "

#Xoá bỏ khoảng trắng
stripped = messy_phone.strip()
#Loại bỏ dấu '-' và khoảng trắng bên trong
replace_phone = stripped.replace("-"," ").replace(" ","")
#In ra số điện thoại chuẩn hóa
print("Số điện thoại đã được chuẩn hoá:",replace_phone)