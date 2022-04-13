from Admin import login_admin, category_admin
import random

admin_username = "admin"
admin_password = "qwer@1234"

admin_categoryname = "Category" + str(random.randint(0,999))

def test_create_category(page):
    login_admin.AdminLogin(page,admin_username,admin_password)
    category_admin.CreateCategory(page, admin_categoryname)
    # Click [placeholder="Select\ the\ property\ search\,\ or\ enter\ a\ keyword\ to\ identify\ the\ search"]
    page.locator("[placeholder=\"Select\\ the\\ property\\ search\\,\\ or\\ enter\\ a\\ keyword\\ to\\ identify\\ the\\ search\"]").click()
    # Fill [placeholder="Select\ the\ property\ search\,\ or\ enter\ a\ keyword\ to\ identify\ the\ search"]
    page.locator("[placeholder=\"Select\\ the\\ property\\ search\\,\\ or\\ enter\\ a\\ keyword\\ to\\ identify\\ the\\ search\"]").fill(admin_categoryname)
    # Click .ant-btn.ant-btn-default >> nth=0
    page.locator(".ant-btn.ant-btn-default").first.click()
     # Click text=categoryname
    content = page.text_content("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div.ant-pro-table > div > table > tbody > tr > td:nth-child(1)")
    assert content == str(admin_categoryname)

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

def test_delete_category(page):
    login_admin.AdminLogin(page,admin_username,admin_password)
    category_admin.CreateCategory(page, admin_categoryname)
    category_admin.DeleteCategory(page, admin_categoryname)
    # Click [placeholder="Select\ the\ property\ search\,\ or\ enter\ a\ keyword\ to\ identify\ the\ search"]
    page.locator("[placeholder=\"Select\\ the\\ property\\ search\\,\\ or\\ enter\\ a\\ keyword\\ to\\ identify\\ the\\ search\"]").click()
    # Fill [placeholder="Select\ the\ property\ search\,\ or\ enter\ a\ keyword\ to\ identify\ the\ search"]
    page.locator("[placeholder=\"Select\\ the\\ property\\ search\\,\\ or\\ enter\\ a\\ keyword\\ to\\ identify\\ the\\ search\"]").fill(admin_categoryname)
    # Click .ant-btn.ant-btn-default >> nth=0
    page.locator(".ant-btn.ant-btn-default").first.click()
    # Click [aria-label="reload"] svg
    page.locator("[aria-label=\"reload\"] svg").click()
    # Click text=admin_subcategoryname
    # page.locator("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div.ant-pro-table > div > table > tbody > tr:nth-child(2) > td:nth-child(1)").click()
    content = page.text_content("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div.ant-pro-table > div > div:nth-child(3)")
    assert content != str(admin_categoryname)

def test_create_subcategory(page):
    login_admin.AdminLogin(page,admin_username,admin_password)
    category_admin.CreateCategory(page, admin_categoryname)
    admin_subcategoryname = "Sub_"+admin_categoryname
    category_admin.CreateSubcategory(page, admin_categoryname, admin_subcategoryname)
    # Click [placeholder="Select\ the\ property\ search\,\ or\ enter\ a\ keyword\ to\ identify\ the\ search"]
    page.locator("[placeholder=\"Select\\ the\\ property\\ search\\,\\ or\\ enter\\ a\\ keyword\\ to\\ identify\\ the\\ search\"]").click()
    # Fill [placeholder="Select\ the\ property\ search\,\ or\ enter\ a\ keyword\ to\ identify\ the\ search"]
    page.locator("[placeholder=\"Select\\ the\\ property\\ search\\,\\ or\\ enter\\ a\\ keyword\\ to\\ identify\\ the\\ search\"]").fill(admin_subcategoryname)
    # Click .ant-btn.ant-btn-default >> nth=0
    page.locator(".ant-btn.ant-btn-default").first.click()
    # Click text=admin_subcategoryname
    page.locator("text="+admin_subcategoryname).click()
    content = page.text_content("text="+admin_subcategoryname)
    assert content == str(admin_subcategoryname)

def test_modify_subcategory(page):
    login_admin.AdminLogin(page,admin_username,admin_password)
    category_admin.CreateCategory(page, admin_categoryname)
    admin_subcategoryname = "Sub_"+admin_categoryname
    category_admin.CreateSubcategory(page, admin_categoryname, admin_subcategoryname)
    admin_new_subcategoryname = "Change_"+admin_subcategoryname
    category_admin.ModifySubcategory(page, admin_subcategoryname, admin_new_subcategoryname)
    # Click [placeholder="Select\ the\ property\ search\,\ or\ enter\ a\ keyword\ to\ identify\ the\ search"]
    page.locator("[placeholder=\"Select\\ the\\ property\\ search\\,\\ or\\ enter\\ a\\ keyword\\ to\\ identify\\ the\\ search\"]").click()
    # Fill [placeholder="Select\ the\ property\ search\,\ or\ enter\ a\ keyword\ to\ identify\ the\ search"]
    page.locator("[placeholder=\"Select\\ the\\ property\\ search\\,\\ or\\ enter\\ a\\ keyword\\ to\\ identify\\ the\\ search\"]").fill(admin_new_subcategoryname)
    # Click .ant-btn.ant-btn-default >> nth=0
    page.locator(".ant-btn.ant-btn-default").first.click()
    # Click [aria-label="reload"] svg
    page.locator("[aria-label=\"reload\"] svg").click()
    # Click text=admin_subcategoryname
    page.locator("text="+admin_new_subcategoryname).click()
    content = page.text_content("text="+admin_new_subcategoryname)
    assert content == str(admin_new_subcategoryname)

def test_delete_subcategory(page):
    login_admin.AdminLogin(page,admin_username,admin_password)
    category_admin.CreateCategory(page, admin_categoryname)
    admin_subcategoryname = "Sub_"+admin_categoryname
    category_admin.CreateSubcategory(page, admin_categoryname, admin_subcategoryname)
    category_admin.DeleteSubcategory(page, admin_subcategoryname)
    # Click [placeholder="Select\ the\ property\ search\,\ or\ enter\ a\ keyword\ to\ identify\ the\ search"]
    page.locator("[placeholder=\"Select\\ the\\ property\\ search\\,\\ or\\ enter\\ a\\ keyword\\ to\\ identify\\ the\\ search\"]").click()
    # Fill [placeholder="Select\ the\ property\ search\,\ or\ enter\ a\ keyword\ to\ identify\ the\ search"]
    page.locator("[placeholder=\"Select\\ the\\ property\\ search\\,\\ or\\ enter\\ a\\ keyword\\ to\\ identify\\ the\\ search\"]").fill(admin_subcategoryname)
    # Click .ant-btn.ant-btn-default >> nth=0
    page.locator(".ant-btn.ant-btn-default").first.click()
    # Click [aria-label="reload"] svg
    page.locator("[aria-label=\"reload\"] svg").click()
    # Click text=admin_subcategoryname
    # page.locator("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div.ant-pro-table > div > table > tbody > tr:nth-child(2) > td:nth-child(1)").click()
    content = page.text_content("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div.ant-pro-table > div > div:nth-child(3)")
    assert content != str(admin_subcategoryname)