from certifi import contents
from Admin import login_admin, roles_admin, user_admin, category_admin
import datetime
import random
import time


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

# def test_delete_role(page):
#     login_admin.AdminLogin(page, admin_username, admin_password)
#     roles_admin.CreateRole(page, admin_rolename, admin_description)
#     roles_admin.DeleteRole(page, admin_rolename)
#     content = page.text_content(".ant-message-notice-content")
#     assert content == "Delete Success!"

# def test_edit_role(page):
#     login_admin.AdminLogin(page, admin_username, admin_password)
#     roles_admin.CreateRole(page, admin_rolename, admin_description)
#     roles_admin.EditRole(page, admin_rolename, admin_description)
#     content = page.text_content(".ant-message-notice-content")
#     assert content == "Edit Success!"

admin_new_username = "Mvtest"+str(random.randint(0,9999))
admin_new_fullname =  admin_new_username+str(time.time())
admin_new_email =  admin_new_username+"@test.co"
admin_new_password = "qwer`123"
# print(f'\nUserName:{admin_new_username}')
# print(f'\nFullname:{admin_new_fullname}')
# print(f'\nEmail:{admin_new_email}')
# print(f'\nPassword:{admin_new_password}')


# def test_create_user(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     user_admin.CreateUser(page, admin_new_username, admin_new_fullname, admin_new_email, admin_new_password)
#     content = page.text_content(".ant-message-notice-content")
#     assert content == "Create User Success!"
    
# def test_edit_user(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     user_admin.CreateUser(page, admin_new_username, admin_new_fullname, admin_new_email, admin_new_password)
#     user_admin.EditUser(page, admin_new_username, admin_new_email)
#     content = page.text_content(".ant-message-notice-content")
#     assert content == "Edit Success!"

# def test_delete_user(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     user_admin.CreateUser(page, admin_new_username, admin_new_fullname, admin_new_email, admin_new_password)
#     user_admin.DeleteUser(page,admin_new_username)
#     content = page.text_content(".ant-message-notice-content")
#     assert content == "user.delete.success"#    文案待换

# def test_reset_password(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     user_admin.CreateUser(page, admin_new_username, admin_new_fullname, admin_new_email, admin_new_password)
#     user_admin.ResetPassword(page, admin_new_username, admin_new_password)
#     content = page.text_content(".ant-message-notice-content")
#     assert content == "Reset Password Success!"

admin_categoryname = "Category" + str(random.randint(0,999))

# def test_create_category(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     category_admin.CreateCategory(page, admin_categoryname)
    # # Click [placeholder="Select\ the\ property\ search\,\ or\ enter\ a\ keyword\ to\ identify\ the\ search"]
    # page.locator("[placeholder=\"Select\\ the\\ property\\ search\\,\\ or\\ enter\\ a\\ keyword\\ to\\ identify\\ the\\ search\"]").click()
    # # Fill [placeholder="Select\ the\ property\ search\,\ or\ enter\ a\ keyword\ to\ identify\ the\ search"]
    # page.locator("[placeholder=\"Select\\ the\\ property\\ search\\,\\ or\\ enter\\ a\\ keyword\\ to\\ identify\\ the\\ search\"]").fill(admin_categoryname)
    # # Click .ant-btn.ant-btn-default >> nth=0
    # page.locator(".ant-btn.ant-btn-default").first.click()
    # # Click [aria-label="reload"] svg
    # page.locator("[aria-label=\"reload\"] svg").click()
    # # Click text=categoryname
    # content = page.text_content("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div.ant-pro-table > div > table > tbody > tr > td:nth-child(1)")
    # assert content == str(admin_categoryname)

def test_modify_category(page):
    login_admin.AdminLogin(page,admin_username,admin_password)
    category_admin.CreateCategory(page, admin_categoryname)
    admin_new_categoryname = "Change"+admin_categoryname
    category_admin.ModifyCategory(page, admin_categoryname, admin_new_categoryname)
    # Click [placeholder="Select\ the\ property\ search\,\ or\ enter\ a\ keyword\ to\ identify\ the\ search"]
    page.locator("[placeholder=\"Select\\ the\\ property\\ search\\,\\ or\\ enter\\ a\\ keyword\\ to\\ identify\\ the\\ search\"]").click()
    # Fill [placeholder="Select\ the\ property\ search\,\ or\ enter\ a\ keyword\ to\ identify\ the\ search"]
    page.locator("[placeholder=\"Select\\ the\\ property\\ search\\,\\ or\\ enter\\ a\\ keyword\\ to\\ identify\\ the\\ search\"]").fill(admin_new_categoryname)
    # Click .ant-btn.ant-btn-default >> nth=0
    page.locator(".ant-btn.ant-btn-default").first.click()
    # Click [aria-label="reload"] svg
    page.locator("[aria-label=\"reload\"] svg").click()
    # Click text=categoryname
    content = page.text_content("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div.ant-pro-table > div > table > tbody > tr > td:nth-child(1)")
    assert content == str(admin_new_categoryname)

def test_create_subcategory(page):