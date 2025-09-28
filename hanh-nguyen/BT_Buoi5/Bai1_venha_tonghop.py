# Viết chương trình yêu cầu người dùng nhập số.
# Nếu nhập đúng → in bình phương.
# Nếu nhập sai → in "Sai định dạng".

try:
    a = float(input('Hãy nhập số: '))
    print("Bình phương của số này là:", a*a)
except ValueError:
    print("Sai định dạng")