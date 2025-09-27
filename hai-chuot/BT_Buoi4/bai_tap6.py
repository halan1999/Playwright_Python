# # NOTE BÀI 6: Cho chuỗi log:
#  log = "ERROR: Login failed at 10:45"

# Kiểm tra trong log có chứa từ "ERROR" hay không (dùng in).
# Nếu có, in ra: "❌ Có lỗi xảy ra".
# Nếu không, in ra: "✅ Hệ thống bình thường".

log = "ERROR: Login failed at 10:45"

check_str = "ERROR"
if check_str in log:
    print("❌ Có lỗi xảy ra")
else:
    print("✅ Hệ thống bình thường")