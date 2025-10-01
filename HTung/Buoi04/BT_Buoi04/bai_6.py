# 6. Cho chuỗi log:
#  log = "ERROR: Login failed at 10:45"

# Kiểm tra trong log có chứa từ "ERROR" hay không (dùng in).
# Nếu có, in ra: "❌ Có lỗi xảy ra".
# Nếu không, in ra: "✅ Hệ thống bình thường".

log = "ERROR: Login failed at 10:45"

checkERROR = "ERROr"
status = False

# kiểm tra từ 
for token_log in log.split():
    # Kiểm tra token có chứa ERROR không
    if checkERROR in token_log :
        status = True
        break

if  status:
    print("❌ Có lỗi xảy ra")
else:
    print("✅ Hệ thống bình thường")
#kiem tra

