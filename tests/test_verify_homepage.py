import re, time
from playwright.sync_api import Page,expect

#import re = regularexpress
#expect la thu vien giup minh so sanh - luon import 2 cai nay

#def tên test case


def test_check_title_google(page: Page):
    # 1️⃣ Truy cập trang web
    print("🤖 Robot bắt đầu mở trình duyệt Google...")
    page.goto("https://www.google.com/")
 
    # 2️⃣ Kiểm tra tiêu đề
    expect(page).to_have_title(re.compile("Google"))
    print("✅ Tiêu đề chính xác: Google")

    # 3️⃣ Kiểm tra URL có chứa “google”
    expect(page).to_have_url(re.compile("google"))
    print("🌐 URL hợp lệ!")
