 	
# 4. Cho chuỗi số điện thoại:
# messy_phone = " 090-123 4567 "
 
# Dùng strip() để bỏ khoảng trắng.
# Dùng replace() để bỏ dấu - và khoảng trắng.
# In ra số điện thoại chuẩn hóa: 0901234567.

messy_phone = " 090-123 4567 "

phone1 = messy_phone.strip()
print(phone1)

phone2 = messy_phone.replace("-","").replace(" ","")
print(phone2)