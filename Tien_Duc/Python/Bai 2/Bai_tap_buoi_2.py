bai1 = [1,2,3,4,5]
print('Tong cua list a la:', sum(bai1))
bai2 = {"name": "Lan", "age": 25, "city": "Hà Nội"}
print(bai2)
a = 10                                                                                                                                                                                                        
b = 3.5                                                                                                                                                                                                        
c = True                                                                                                                                                                                                        
d = None                                                                                                                                                                                                        
e = "Python"
print(type(a), type(b), type(c), type(d), type(e))
score = [9, 7, 10, 8, 6]
print(max(score), sum(score)/len(score))
score.append(5)
birthday = (11, 9, 2025)
print('ngay',birthday[0],'thang',birthday[1],'nam',birthday[2])
student = {"name": "Lan", "age": 18, "email": "lan@gmail.com"}
print('Ten la:', student["name"], 'email la:', student["email"])
emails = {"a@gmail.com", "b@gmail.com", "a@gmail.com"}
print(emails)
#set in ra khong trung nhau
emails.add('d@gmail.com')
print(emails)
# remove la xoa khoi set, discard la xoa khoi set neu co, neu khong co thi khong bao loi
