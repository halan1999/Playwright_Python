try:
   a=float(input("nhap so a:"))
   result=a**2
   print(f"{a} bình phương là : {result}")
except ValueError as e:
       print("Vui long nhap đúng định dạng:",e)
