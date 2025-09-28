numbers=[2,5,8,11,14,17,20]
print("Các số trong list là",numbers)
print("Các số chẵn trong list là:")
for num in numbers:
    if num%2==0:
        print(num)
print("Tổng các số trong list là:", sum(numbers))
for num in numbers:
    print("Bảng cửu chương của",num)
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")
    print("-------")