from Admin import login_admin, roles_admin
import datetime
import random

admin_username = "admin"
admin_password = "qwer@1234"

admin_rolename = "Role"+str(random.randint(0,9999))
admin_description = admin_rolename + str(datetime.datetime.now().timestamp())

def test_create_role(page):
    login_admin.AdminLogin(page, admin_username, admin_password)
    roles_admin.CreateRole(page, admin_rolename, admin_description)
    # Click .ant-message-notice-content
    page.locator(".ant-message-notice-content").click()
    content = page.text_content(".ant-message-notice-content")
    if content == "Create Success!":
        print(f'\nSuccess')
    else:
        print(f'\nFailed')
    assert content == "Create Success!"