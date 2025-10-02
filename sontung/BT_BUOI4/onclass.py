# Bài 1
user_email = "automation.tester01@g-mail.com"

emailParse = user_email.split("@")

print("username: ", emailParse[0])

# Bài 2
messy_phone = " 090-123 4567 "

phone = messy_phone.replace(" ", "").replace("-", "")

print("SĐT sau khi chuẩn hóa: ", phone)

# Bài 3
title = "Top 5 Laptop Gaming Đáng Mua Nhất"

slug = title.lower().replace(" ", "-")

print("Slug: ", slug)
