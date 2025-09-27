expected_messages = ['login successfull ', 'welcome']
actual_messages = 'welcome'
if actual_messages == expected_messages:
    print ('Messages hop le')
else:
    print ('Messages khong hop le')

for i in range (1, 101):
    if i % 7 == 0:
        print (i)
        break

score = [95, 82, 67, 45, 88, 90, 50]
for i in score:
    if i >= 90:
        print(i,': Xuat sac')
    elif i >= 70:
        print(i,': Kha')
    elif i >= 50:
        print(i,': Trung binh')
    else:
        print(i,': Yeu')

for i in range(1, 11):
    b = 2 * i
    c = 3 * i 
    print(f"bang cuu chuong 2*{i} = {b}")
    print(f"bang cuu chuong 3*{i} = {c}")

