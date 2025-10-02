#1
user_email = "automation.tester01@g-mail.com"
print(user_email[0:19])
#2
messy_phone = " 090-123 4567 "
phone = messy_phone.replace("-","").replace(" ", "")
print("So dien thoai:", phone)
#3
s = "Top 5 Laptop Gaming Dang Mua Nhat"
t = s.replace(" ", "-")
f = t.lower()
print(f)
