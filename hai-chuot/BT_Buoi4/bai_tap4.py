# NOTE BÀI 4: Cho chuỗi số điện thoại:
# messy_phone = " 090-123 4567 "
 
# Dùng strip() để bỏ khoảng trắng.
# Dùng replace() để bỏ dấu - và khoảng trắng.
# In ra số điện thoại chuẩn hóa: 0901234567.

messy_phone = " 090-123 4567 "

# Loại bỏ khoảng trắng đầu cuối".
print(messy_phone.strip())

# Bỏ dấu - và khoảng trắng kết hợp chuẩn hóa chuỗi".
new_text = messy_phone.strip()
new_text = new_text.replace("-", "")
new_text = new_text.replace(" ", "")
print(new_text)