try:
    btn = driver.find_element(By.ID, "submit")
    btn.click()
except NoSuchElementException:
    print("Không tìm thấy element")
else:
    print("Đã tìm thấy element!")
finally:
    print("Đóng trình duyệt")
