from Admin import login_admin, user_admin
import random
import time

admin_username = "admin"
admin_password = "qwer@1234"

admin_new_username = "Mvtest"+str(random.randint(0,9999))
admin_new_fullname =  admin_new_username+str(time.time())
admin_new_email =  admin_new_username+"@test.co"
admin_new_password = "qwer`123"
# print(f'\nUserName:{admin_new_username}')
# print(f'\nFullname:{admin_new_fullname}')
# print(f'\nEmail:{admin_new_email}')
# print(f'\nPassword:{admin_new_password}')

def test_create_user(page):
    login_admin.AdminLogin(page,admin_username,admin_password)
    user_admin.CreateUser(page, admin_new_username, admin_new_fullname, admin_new_email, admin_new_password)
    content = page.text_content(".ant-message-notice-content")
    assert content == "Create User Success!"

def test_edit_user(page):
    login_admin.AdminLogin(page,admin_username,admin_password)
    user_admin.CreateUser(page, admin_new_username, admin_new_fullname, admin_new_email, admin_new_password)
    user_admin.EditUser(page, admin_new_username, admin_new_email)
    content = page.text_content(".ant-message-notice-content")
    assert content == "Edit Success!"

def test_delete_user(page):
    login_admin.AdminLogin(page,admin_username,admin_password)
    user_admin.CreateUser(page, admin_new_username, admin_new_fullname, admin_new_email, admin_new_password)
    user_admin.DeleteUser(page,admin_new_username)
    content = page.text_content(".ant-message-notice-content")
    assert content == "user.delete.success"#    User deleted successfully

def test_reset_password(page):
    login_admin.AdminLogin(page,admin_username,admin_password)
    user_admin.CreateUser(page, admin_new_username, admin_new_fullname, admin_new_email, admin_new_password)
    user_admin.ResetPassword(page, admin_new_username, admin_new_password)
    content = page.text_content(".ant-message-notice-content")
    assert content == "Reset Password Success!"