# Danh sach messages
expected_messages = ['Login succesfull', 'Welcome'] 
# Messages thuc te
actual_message = 'Welcome'
# Check
if actual_message in expected_messages:
    print("Message valid")
else:
    print("Message invalid") 
