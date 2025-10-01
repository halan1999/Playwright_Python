a = input("Nhap a: ")
b = input("Nhap b: ")
try:
    a = float(a)
    b = float(b)
    c = a / b
    print('a chia b bang:',c)
except (ValueError,ZeroDivisionError) as e:
    print('Loi, ly do:', e)


