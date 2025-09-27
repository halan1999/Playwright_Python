text = "  hello world  "
clean_text = text.strip()
print(len(text))
print(clean_text)

name = "Nguyễn Tiến Đức"
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())

s = "Automation Testing"
print(s[0:10])
print(s[11:19])
print(s[0:5])
print(s[13:19])

messy_phone = " 090-123 4567 "
b = messy_phone.strip()
c = b.replace("-", "")
d = c.replace(" ", "")
print(d)

fruits = ["apple", "banana", "cherry"]
noi = (', ').join(fruits)
print(noi)   

log = "ERROR: Login failed at 10:45"
if "ERROR" in log:
    print("Co loi xay ra")
else:
    print("He thong binh thuong")