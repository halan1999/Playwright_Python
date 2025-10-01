# 2. Cho chuỗi:  name = "tên bạn"
# In ra chữ hoa toàn bộ.
# In ra chữ thường toàn bộ.
# In ra dạng capitalize (chữ cái đầu viết hoa).
# In ra dạng title (mỗi từ viết hoa chữ cái đầu).

# Cho chuỗi
name = " tên bạn"
names = "Thứ Ba"

#In ra chữ hoa toàn bộ
print("In ra chữ hoa:", name.upper())
print("-"*50)

#In ra chữ thường toàn bộ.
print("In ra chữ thường:",names.lower())
print("-"*50)

# In ra dạng capitalize (chữ cái đầu viết hoa).
print("Chữ cái đầu viết HOA:",name.capitalize())
print("-"*50)

# In ra dạng title (mỗi từ viết hoa chữ cái đầu).
print("Viết hoa chữ cái đầu:",name.title())
print("-"*50)

#---------------------------
# Áp dụng strip() và điều kiện vào.
name  = "  tên của tôi  "
# xoá bỏ khoảng trắng trước
name= name.strip()
i = 1
if not name:
    print("Bạn cần phải nhận tên.")
elif len(name) > i:
    print("Chuyển sang chữ HOA:", name.upper())
    print ("-"*50)
else:
    print("Viết hoa chữ đầu mỗi từ:", name.title())
    print ("-"*50)