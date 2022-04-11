from Admin import login_admin, roles_admin
import datetime
import random

admin_username = "admin"
admin_password = "qwer@1234"

# def test_admin_login(page):
#     login_admin.AdminLogin(page, admin_username, admin_password)
#     page.goto("https://admin-banana-test.chunsutech.com/dashboard")
#     page.locator("#root > div > section > div.ant-layout > main > div").click()
#     content = page.text_content("#root > div > section > div.ant-layout > main > div")
#     assert content == "Hello"

# def test_admin_logout(page):
#     login_admin.AdminLogin(page, admin_username, admin_password)
#     login_admin.AdminLogout(page)
#     page.locator("#root > div > div > form > div.ant-row.ant-form-item.myButton___3IouX > div > div > div > button > span").click()
#     content = page.text_content("#root > div > div > form > div.ant-row.ant-form-item.myButton___3IouX > div > div > div > button > span")
#     assert content == "Submit"


admin_rolename = "Role"+str(random.randint(0,999))
admin_description = admin_rolename +" ; "+ str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print(f'\nadmin_rolename:,{admin_rolename}')
print(f'\nadmin_description:,{admin_description}')

# def test_create_role(page):
#     login_admin.AdminLogin(page, admin_username, admin_password)
#     roles_admin.CreateRole(page, admin_rolename, admin_description)
#     # Click .ant-message-notice-content
#     page.locator(".ant-message-notice-content").click()
#     content = page.text_content(".ant-message-notice-content")
#     assert content == "Create Success!"

# def test_seaerch_role(page):
#     login_admin.AdminLogin(page, admin_username, admin_password)
#     roles_admin.CreateRole(page, admin_rolename, admin_description)
#     roles_admin.SearchRole(page, admin_rolename)
#     content = page.text_content("text=" + admin_rolename)
#     assert content == str(admin_rolename)

def test_delete_role(page):
    login_admin.AdminLogin(page, admin_username, admin_password)
    roles_admin.CreateRole(page, admin_rolename, admin_description)
    roles_admin.DeleteRole(page, admin_rolename)
    content = page.text_content(".ant-message-notice-content")
    assert content == "Delete Success!"