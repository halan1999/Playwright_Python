#  Cho chuối số điện thoại 
messy_phone = " 090-123 4567 "
# Dùng strip() để bỏ khoảng trắng.
del_phone = messy_phone.strip()
# Dùng replace() để bỏ dấu gạch ngang và khoảng trắng
clean_phone = del_phone.replace("-", "").replace(" ", "")
# In ra số điện thoại được chuẩn hóa
print(clean_phone)  # Output: "0901234567"

