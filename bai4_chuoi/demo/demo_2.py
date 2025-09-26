# Chuẩn hóa số điện thoại: Một SĐT được nhập vào có dạng messy_phone = " 090-123 4567 ". Hãy viết code để chuẩn hóa SĐT này về dạng 0901234567 (loại bỏ hết khoảng trắng và gạch nối).
messy_phone = " 090-123 4567 "
# cleaned_phone = messy_phone.replace(" ", "").replace("-", "")
# print(cleaned_phone)
phone1=messy_phone.strip()
phone2=phone1.replace("-","")
cleaned_phone=phone2.replace(" ","")
print(cleaned_phone)
