# 4. Cho chuỗi số điện thoại:
# messy_phone = " 090-123 4567 "
messy_phone = " 090-123 4567 "
# Dùng strip() để bỏ khoảng trắng.
messy_phone=messy_phone.strip()
# Dùng replace() để bỏ dấu - và khoảng trắng.
messy_phone=messy_phone.replace("-", " ")
messy_phone=messy_phone.replace(" ", "")
# In ra số điện thoại chuẩn hóa: 0901234567.
print(f"Số điện thoại sau khi chuẩn hóa:",messy_phone)