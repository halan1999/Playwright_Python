emails={"a@gmail.com","b@gmail.com","c@gmail.com"}
print(emails)
emails.add("d@gmail.com")
print(emails)
emails.remove("d@gmail.com") # Nếu không tồn tại thì báo lỗi
print(emails)
emails.discard("d@gmail.com")#clea Nếu không tồn tại thì không báo lỗi
print(emails)