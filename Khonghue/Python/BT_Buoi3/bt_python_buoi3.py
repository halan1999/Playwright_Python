#1. Tim sản phẩm trong list
products = ["iphone 13", "samsung galaxy", "macbook 16 inch", "oppe reno"]
flag = False # Co danh dau
for sp in products:
    if sp == "macbook 16 inch":
        flag = True
        break
if flag:
    print("Da tim thay san pham")
else :
    print("Khong tim thay san pham")

#2. 
numbers = [2,5,8,11,14,17,20]
#in list
print (numbers)
#in số chẵn
for n in numbers:
    if n % 2 == 0 :
        print("La so chan:", n)
#Tinh tổng
print(sum(numbers))
#in bản cửu chương
for c in numbers:
    for i in range (1,11): 
        print("Bang cuu chuong cac so:", i * c)
