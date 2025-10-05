# print("**************** Kết quả bài 1 ****************")
# text = "  hello world  "
# print(f"Chiều dài của '{text}' là {len(text)}")
# text_strip = text.strip()
# print(f"Chiều dài của '{text_strip}' là {len(text_strip)}")

# print("\n**************** Kết quả bài 2 ****************")
# name = "Nguyễn Thoại Kiều Tâm"
# print(f"Name = '{name}'")
# print(f"In hoa là {name.upper()}")
# print(f"In chữ thường là {name.lower()}")
# print(f"In chữ cái đầu viết hoa là {name.capitalize()}")
# print(f"In mỗi từ viết hoa chữ cái đầu là {name.title()}")

# print("\n**************** Kết quả bài 3 ****************")
# s = "Automation Testing"
# print(s[:10])
# print(s[11:18])
# print(s[:5])
# print(s[-3:])

# print("\n**************** Kết quả bài 4 ****************")
# messy_phone = " 090-123 4567 "
# messy_phone_strip = messy_phone.strip().replace("-","").replace(" ","")
# print(f"In ra số điện thoại chuẩn hóa của '{messy_phone}' là {messy_phone_strip}")

# print("\n**************** Kết quả bài 5 ****************")
# fruits = ["apple", "banana", "cherry"]
# result = ", ".join(fruits)
# print(result)

# print("\n**************** Kết quả bài 6 ****************")
# log = "ERROR: Login failed at 10:45"
# if "ERROR" in log:
#     print("❌ Có lỗi xảy ra")
# else:
#     print("✅ Hệ thống bình thường")

log = "SUCCESS: Login success"
log = "ERROR: Login failed at 10:45"
if "SUCCESS" in log:
    print("✅ Test case : Passed")
else:
    print("❌ Test case : Failed")
