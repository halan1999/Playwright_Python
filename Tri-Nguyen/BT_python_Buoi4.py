#bai 1
print("Bài 1 --------------")
text = "hello world"
count_text = len(text)
print(f"số lượng ký tự trong chuỗi là: {count_text}")

#bai 2
print("Bài 2 --------------")
name = "ten ban"
upper_name = name.upper()
lower_name = name.lower()
capitalize_name = name.capitalize()
title_name = name.title()

print(upper_name)
print(lower_name)
print(capitalize_name)
print(title_name)

#bai 3
print("Bài 3 --------------")
s = "Automation Testing"
print("Cách giải 1 ---------")
Automation_text = s[0:11]
Get_text = s.find("T")
Testing_text = s[Get_text:Get_text + 8]
First_five_letter = s[0:5]
Last_three_letter = s[15:18]

print(Automation_text)
print(Testing_text)
print(First_five_letter)
print(Last_three_letter)

print("Cách giải 2 ---------")
automation_text = s.split()[0]
testing_text = s.split()[1]
first_five_letter = s[:5]
last_three_letter = s[-3:]

print(automation_text)
print(testing_text)
print(first_five_letter)
print(last_three_letter)


#bai 4
print("Bài 4 --------------")
messy_phone = " 090-123 4567 "

remove_space = messy_phone.strip()
replace_special_letter = messy_phone.replace("-","").replace(" ","")

print(remove_space)
print(replace_special_letter)

#bai 5
print("Bài 5 --------------")
fruits = ["apple", "banana", "cherry"]
join_fruits = ",".join(fruits)

print(join_fruits)

#bai 6

print("Bài 6 --------------")
print("Cách giải 1 ---------")
log = "ERROR: Login failed at 10:45"
check_error = "ERROR"
set_flag = False
if check_error in log:
 set_flag = True
else:
 set_flag = False

if set_flag:
 print("Có lỗi xảy ra")
else:
 print("Hệ thống bình thường")

print("Cách giải 2 ---------")
if check_error in log:
 print("Có lỗi xảy ra")
else:
 print("Hệ thống bình thường")