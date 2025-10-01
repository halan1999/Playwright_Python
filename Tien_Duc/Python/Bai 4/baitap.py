user_email = "automation.tester01@g-mail.com"
a = user_email[0:19]
print(a)

messy_phone = " 090-123 4567 "
b = messy_phone.strip()
c = b.replace("-", "")
d = c.replace(" ", "")
print(d)

thaythe = "Top 5 Laptop Gaming Đáng Mua Nhất"
e = thaythe.replace(" ", "-")
f = e.lower()
print(f)