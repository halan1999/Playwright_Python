# Tạo slug URL: "Slug" là phiên bản rút gọn của tiêu đề, dùng cho URL. Ví dụ, tiêu đề "Top 5 Laptop Gaming Đáng Mua Nhất" sẽ có slug là "top-5-laptop-gaming-dang-mua-nhat". Hãy viết code để chuyển đổi một tiêu đề bất kỳ thành slug theo quy tắc:

# Chuyển hết về chữ thường.

# Thay thế tất cả khoảng trắng bằng dấu gạch ngang (-).
Sluf_title="Top 5 Laptop Gaming Đáng Mua Nhất"
sluf=Sluf_title.lower().replace(" ","-")
print(sluf)