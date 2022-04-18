from Admin import login_admin, resources_admin
from datetime import datetime
import time

admin_username = "admin"
admin_password = "qwer@1234"

admin_groupname = "Group"+str(int(time.time()))

def test_add_group(page):
    login_admin.AdminLogin(page,admin_username,admin_password)
    resources_admin.AddGroup(page, admin_groupname)
    # Click .ant-message-notice-content
    page.locator(".ant-message-notice-content").click()
    content = page.text_content(".ant-message-notice-content")
    assert content == "Create Group Success!"

def test_add_subgroup(page):
    login_admin.AdminLogin(page,admin_username,admin_password)
    resources_admin.AddGroup(page, admin_groupname)
    admin_subgroupname = "Sub_"+admin_groupname
    resources_admin.AddSubgroup(page, admin_groupname, admin_subgroupname)
    # Click .ant-message-notice-content
    page.locator(".ant-message-notice-content").click()
    content = page.text_content(".ant-message-notice-content")
    assert content == "Create Group Success!"

def test_change_subgroup(page):
    login_admin.AdminLogin(page,admin_username,admin_password)
    resources_admin.AddGroup(page, admin_groupname)
    admin_subgroupname = "Sub_"+admin_groupname
    resources_admin.AddSubgroup(page, admin_groupname, admin_subgroupname)
    admin_new_subgroupname = "ChangeSub"+str(int(time.time()))
    resources_admin.ChangeSubgroup(page, admin_subgroupname, admin_new_subgroupname)
    # Click .ant-message-notice-content
    page.locator(".ant-message-notice-content").click()
    content = page.text_content(".ant-message-notice-content")
    assert content == "Change Group Success!"

def test_delete_subgroup(page):
    login_admin.AdminLogin(page,admin_username,admin_password)
    resources_admin.AddGroup(page, admin_groupname)
    admin_subgroupname = "Sub_"+admin_groupname
    resources_admin.AddSubgroup(page, admin_groupname, admin_subgroupname)
    resources_admin.DeleteSubgroup(page, admin_subgroupname)
    # Click .ant-message-notice-content
    page.locator(".ant-message-notice-content").click()
    content = page.text_content(".ant-message-notice-content")
    assert content == "Delete Group Success!"

def test_delete_group(page):
    login_admin.AdminLogin(page,admin_username,admin_password)
    resources_admin.AddGroup(page, admin_groupname)
    resources_admin.DeleteGroup(page, admin_groupname)
    # Click .ant-message-notice-content
    page.locator(".ant-message-notice-content").click()
    content = page.text_content(".ant-message-notice-content")
    assert content == "Delete Group Success!"

def test_add_image(page):
    login_admin.AdminLogin(page,admin_username,admin_password)
    resources_admin.AddGroup(page, admin_groupname)
    resources_admin.AddImage(page, admin_groupname)
    page.locator(".ant-message-notice-content").click()
    content = page.text_content(".ant-message-notice-content")
    assert content == "Add Image Success!"

def test_change_imagegroup(page):
    login_admin.AdminLogin(page,admin_username,admin_password)
    resources_admin.AddGroup(page, admin_groupname)
    resources_admin.AddImage(page, admin_groupname)
    resources_admin.ChangeImageGroup(page, admin_groupname)
    page.locator(".ant-message-notice-content").click()
    content = page.text_content(".ant-message-notice-content")
    assert content == "Change Group Success!"

def test_delete_image(page):
    login_admin.AdminLogin(page,admin_username,admin_password)
    resources_admin.AddGroup(page, admin_groupname)
    resources_admin.AddImage(page, admin_groupname)
    resources_admin.DeleteImage(page, admin_groupname)
    page.locator(".ant-message-notice-content").click()
    content = page.text_content(".ant-message-notice-content")
    assert content == "Delete Success!"