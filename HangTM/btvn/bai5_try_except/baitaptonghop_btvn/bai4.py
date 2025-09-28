# Giả lập tìm element "submit".

# Nếu không tìm thấy → in "Không tìm thấy element".

# Luôn in "Đóng trình duyệt".
try:
    element = None  # Giả lập không tìm thấy element
    if element is None:
        print("Không tìm thấy element")
    else:
        print("Element found")
except Exception as e:
    print(f"Lỗi: {e}")