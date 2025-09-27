emails = {"a@gmail.com", "b@gmail.com", "a@gmail.com"}
print(emails)
emails.add("c@gmail.com")
emails.discard("d@gmail.com")
print("Sau khi discard:", emails)
print(emails.remove("d@gmail.com"))
#remove sẽ báo lỗi còn discard thì không