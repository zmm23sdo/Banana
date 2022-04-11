from Admin import login_admin

admin_username = "admin"
admin_password = "qwer@1234"

def test_admin_login(page):
    login_admin.AdminLogin(page, admin_username, admin_password)
    page.goto("https://admin-banana-test.chunsutech.com/dashboard")
    page.locator("#root > div > section > div.ant-layout > main > div").click()
    content = page.text_content("#root > div > section > div.ant-layout > main > div")
    assert content == "Hello"

def test_admin_logout(page):
    login_admin.AdminLogin(page, admin_username, admin_password)
    login_admin.AdminLogout(page)
    page.locator("#root > div > div > form > div.ant-row.ant-form-item.myButton___3IouX > div > div > div > button > span").click()
    content = page.text_content("#root > div > div > form > div.ant-row.ant-form-item.myButton___3IouX > div > div > div > button > span")
    assert content == "Submit"