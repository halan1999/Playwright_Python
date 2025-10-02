#scores={6,8,7,6,5,9}
#print(scores)
#thao tac voi set
#students={"Nam","Hung","Hoa","Hoa"}
#add them phan tu
#students.add("Lan")
# Xoa phan tu
# If the element is not found, remove() will raise a KeyError.
#students.remove("Nam")
# If the element is not found, discard() will NOT raise an error.
#students.discard("HoaNotExist")
#print(students)
# Dung set trong toan hoc
A={1,2,3,4,5}
B={4,5,6,7,8}
# Hop cua A va B
print(A|B)
# Giao cua A va B
print(A&B)
# Hieu cua A va B : Chi lay phan tu cua A ma khong co trong B
print(A-B)
# Hieu cua B va A : Chi lay phan tu cua B ma khong co trong A
print(B-A)
# Hieu doi xung cua A va B : Lay phan tu khong trung nhau
print(A^B)