from Admin import login_admin, roles_admin
import datetime
import random

admin_username = "admin"
admin_password = "qwer@1234"

admin_rolename = "Role"+str(random.randint(0,9999))
admin_description = admin_rolename + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def test_create_role(page):
    login_admin.AdminLogin(page, admin_username, admin_password)
    roles_admin.CreateRole(page, admin_rolename, admin_description)
    # Click .ant-message-notice-content
    page.locator(".ant-message-notice-content").click()
    content = page.text_content(".ant-message-notice-content")
    assert content == "Create Success!"

def test_seaerch_role(page):
    login_admin.AdminLogin(page, admin_username, admin_password)
    roles_admin.CreateRole(page, admin_rolename, admin_description)
    roles_admin.SearchRole(page, admin_rolename)
    content = page.text_content("text=" + admin_rolename)
    assert content == str(admin_rolename)

def test_delete_role(page):
    login_admin.AdminLogin(page, admin_username, admin_password)
    roles_admin.CreateRole(page, admin_rolename, admin_description)
    roles_admin.DeleteRole(page, admin_rolename)
    content = page.text_content(".ant-message-notice-content")
    assert content == "Delete Success!"