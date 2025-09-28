# Cho chuỗi log:
# log = "ERROR: Login failed at 10:45"
log = "ERROR: Login failed at 10:45"
# Kiểm tra trong log có chứa từ "ERROR" hay không (dùng in).
print("ERROR" in log)  # Output: True
# Nếu có, in ra: "❌ Có lỗi xảy ra".
if "ERROR" in log:
    print("❌ Có lỗi xảy ra")
# Nếu không, in ra: "✅ Hệ thống bình thường"
else:
    print("✅ Hệ thống bình thường")
