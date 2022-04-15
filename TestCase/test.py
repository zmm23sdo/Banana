from certifi import contents
from Admin import login_admin, roles_admin, user_admin, category_admin, product_admin
import datetime
import random
import time


admin_username = "admin"
admin_password = "qwer@1234"

# def test_admin_login(page):
#     login_admin.AdminLogin(page, admin_username, admin_password)
#     page.goto("https://admin-banana-dev.chunsutech.com/dashboard")
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

# def test_modify_category(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     category_admin.CreateCategory(page, admin_categoryname)
#     admin_new_categoryname = "Change"+admin_categoryname
#     category_admin.ModifyCategory(page, admin_categoryname, admin_new_categoryname)
#     # Click [placeholder="Select\ the\ property\ search\,\ or\ enter\ a\ keyword\ to\ identify\ the\ search"]
#     page.locator("[placeholder=\"Select\\ the\\ property\\ search\\,\\ or\\ enter\\ a\\ keyword\\ to\\ identify\\ the\\ search\"]").click()
#     # Fill [placeholder="Select\ the\ property\ search\,\ or\ enter\ a\ keyword\ to\ identify\ the\ search"]
#     page.locator("[placeholder=\"Select\\ the\\ property\\ search\\,\\ or\\ enter\\ a\\ keyword\\ to\\ identify\\ the\\ search\"]").fill(admin_new_categoryname)
#     # Click .ant-btn.ant-btn-default >> nth=0
#     page.locator(".ant-btn.ant-btn-default").first.click()
#     # Click [aria-label="reload"] svg
#     page.locator("[aria-label=\"reload\"] svg").click()
#     # Click text=categoryname
#     content = page.text_content("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div.ant-pro-table > div > table > tbody > tr > td:nth-child(1)")
#     assert content == str(admin_new_categoryname)

# def test_delete_category(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     category_admin.CreateCategory(page, admin_categoryname)
#     category_admin.DeleteCategory(page, admin_categoryname)
#     # Click [placeholder="Select\ the\ property\ search\,\ or\ enter\ a\ keyword\ to\ identify\ the\ search"]
#     page.locator("[placeholder=\"Select\\ the\\ property\\ search\\,\\ or\\ enter\\ a\\ keyword\\ to\\ identify\\ the\\ search\"]").click()
#     # Fill [placeholder="Select\ the\ property\ search\,\ or\ enter\ a\ keyword\ to\ identify\ the\ search"]
#     page.locator("[placeholder=\"Select\\ the\\ property\\ search\\,\\ or\\ enter\\ a\\ keyword\\ to\\ identify\\ the\\ search\"]").fill(admin_categoryname)
#     # Click .ant-btn.ant-btn-default >> nth=0
#     page.locator(".ant-btn.ant-btn-default").first.click()
#     # Click [aria-label="reload"] svg
#     page.locator("[aria-label=\"reload\"] svg").click()
#     # Click text=admin_subcategoryname
#     # page.locator("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div.ant-pro-table > div > table > tbody > tr:nth-child(2) > td:nth-child(1)").click()
#     content = page.text_content("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div.ant-pro-table > div > div:nth-child(3)")
#     assert content != str(admin_categoryname)

# def test_create_subcategory(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     category_admin.CreateCategory(page, admin_categoryname)
#     admin_subcategoryname = "Sub_"+admin_categoryname
#     category_admin.CreateSubcategory(page, admin_categoryname, admin_subcategoryname)
#     # Click [placeholder="Select\ the\ property\ search\,\ or\ enter\ a\ keyword\ to\ identify\ the\ search"]
#     page.locator("[placeholder=\"Select\\ the\\ property\\ search\\,\\ or\\ enter\\ a\\ keyword\\ to\\ identify\\ the\\ search\"]").click()
#     # Fill [placeholder="Select\ the\ property\ search\,\ or\ enter\ a\ keyword\ to\ identify\ the\ search"]
#     page.locator("[placeholder=\"Select\\ the\\ property\\ search\\,\\ or\\ enter\\ a\\ keyword\\ to\\ identify\\ the\\ search\"]").fill(admin_subcategoryname)
#     # Click .ant-btn.ant-btn-default >> nth=0
#     page.locator(".ant-btn.ant-btn-default").first.click()
#     # Click text=admin_subcategoryname
#     page.locator("text="+admin_subcategoryname).click()
#     content = page.text_content("text="+admin_subcategoryname)
#     assert content == str(admin_subcategoryname)

# def test_modify_subcategory(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     category_admin.CreateCategory(page, admin_categoryname)
#     admin_subcategoryname = "Sub_"+admin_categoryname
#     category_admin.CreateSubcategory(page, admin_categoryname, admin_subcategoryname)
#     admin_new_subcategoryname = "Change_"+admin_subcategoryname
#     category_admin.ModifySubcategory(page, admin_subcategoryname, admin_new_subcategoryname)
#     # Click [placeholder="Select\ the\ property\ search\,\ or\ enter\ a\ keyword\ to\ identify\ the\ search"]
#     page.locator("[placeholder=\"Select\\ the\\ property\\ search\\,\\ or\\ enter\\ a\\ keyword\\ to\\ identify\\ the\\ search\"]").click()
#     # Fill [placeholder="Select\ the\ property\ search\,\ or\ enter\ a\ keyword\ to\ identify\ the\ search"]
#     page.locator("[placeholder=\"Select\\ the\\ property\\ search\\,\\ or\\ enter\\ a\\ keyword\\ to\\ identify\\ the\\ search\"]").fill(admin_new_subcategoryname)
#     # Click .ant-btn.ant-btn-default >> nth=0
#     page.locator(".ant-btn.ant-btn-default").first.click()
#     # Click text=admin_subcategoryname
#     page.locator("text="+admin_new_subcategoryname).click()
#     content = page.text_content("text="+admin_new_subcategoryname)
#     assert content == str(admin_new_subcategoryname)

# def test_delete_subcategory(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     category_admin.CreateCategory(page, admin_categoryname)
#     admin_subcategoryname = "Sub_"+admin_categoryname
#     category_admin.CreateSubcategory(page, admin_categoryname, admin_subcategoryname)
#     category_admin.DeleteSubcategory(page, admin_subcategoryname)
#     # Click [placeholder="Select\ the\ property\ search\,\ or\ enter\ a\ keyword\ to\ identify\ the\ search"]
#     page.locator("[placeholder=\"Select\\ the\\ property\\ search\\,\\ or\\ enter\\ a\\ keyword\\ to\\ identify\\ the\\ search\"]").click()
#     # Fill [placeholder="Select\ the\ property\ search\,\ or\ enter\ a\ keyword\ to\ identify\ the\ search"]
#     page.locator("[placeholder=\"Select\\ the\\ property\\ search\\,\\ or\\ enter\\ a\\ keyword\\ to\\ identify\\ the\\ search\"]").fill(admin_subcategoryname)
#     # Click .ant-btn.ant-btn-default >> nth=0
#     page.locator(".ant-btn.ant-btn-default").first.click()
#     # Click [aria-label="reload"] svg
#     page.locator("[aria-label=\"reload\"] svg").click()
#     # Click text=admin_subcategoryname
#     # page.locator("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div.ant-pro-table > div > table > tbody > tr:nth-child(2) > td:nth-child(1)").click()
#     content = page.text_content("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div.ant-pro-table > div > div:nth-child(3)")
#     assert content != str(admin_subcategoryname)

admin_productname = "Product"+str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
admin_product_description = "Product Description:\n\t"+admin_productname+"\n\t"+str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
admin_product_price = "300" 
admin_product_stock = "100" 
admin_product_weight = "1" 
admin_product_freight = "10"

# def test_create_product_basic(page): 
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
#     # Go to https://admin-banana-dev.chunsutech.com/commodity/list
#     page.goto("https://admin-banana-dev.chunsutech.com/commodity/list")
#     # Fill [placeholder="Select\ the\ property\ search\,\ or\ enter\ a\ keyword\ to\ identify\ the\ search"]
#     page.locator("[placeholder=\"Select\\ the\\ property\\ search\\,\\ or\\ enter\\ a\\ keyword\\ to\\ identify\\ the\\ search\"]").fill("productname1234567890")
#     # Click text=CreateAdvanced Search >> button >> nth=1
#     page.locator("text=CreateAdvanced Search >> button").nth(1).click()
#     # Click text=productname1234567890
#     page.locator("text="+admin_productname).click()    
#     content = page.text_content("text="+admin_productname)
#     assert content == str(admin_productname)

admin_product_brand = "Brand"+str(int(time.time()))
admin_variation0 = "0Variation"+str(int(time.time()))
admin_option0 = "0option"+str(int(time.time()))
admin_variation1 = "1Variation"+str(int(time.time()))
admin_option3 = "3option"+str(int(time.time()))
admin_product_sku = "sku_"+str(int(time.time()))
admin_product_barcode = "barcode_"+str(int(time.time()))

# def test_create_product_advance(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     product_admin.CreateProductAdvance(page, admin_productname, admin_product_description, admin_product_brand, admin_variation0,
#                          admin_option0, admin_variation1, admin_option3, admin_product_price,
#                          admin_product_stock, admin_product_weight, admin_product_sku, admin_product_barcode)
#     # Go to https://admin-banana-dev.chunsutech.com/commodity/list
#     page.goto("https://admin-banana-dev.chunsutech.com/commodity/list")
#     # Fill [placeholder="Select\ the\ property\ search\,\ or\ enter\ a\ keyword\ to\ identify\ the\ search"]
#     page.locator("[placeholder=\"Select\\ the\\ property\\ search\\,\\ or\\ enter\\ a\\ keyword\\ to\\ identify\\ the\\ search\"]").fill(admin_productname)
#     # Click text=CreateAdvanced Search >> button >> nth=1
#     page.locator("text=CreateAdvanced Search >> button").nth(1).click()
#     # Click text=productname1234567890
#     page.locator("text="+admin_productname).click()    
#     content = page.text_content("text="+admin_productname)
#     assert content == str(admin_productname)

# def test_change_product(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
#     admin_new_productname =  "Change"+admin_productname
#     admin_new_product_description = "Change"+admin_product_description
#     product_admin.ChangeProduct(page, admin_productname, admin_new_productname, admin_new_product_description)
#     # Go to https://admin-banana-dev.chunsutech.com/commodity/list
#     page.goto("https://admin-banana-dev.chunsutech.com/commodity/list")
#     # Fill [placeholder="Select\ the\ property\ search\,\ or\ enter\ a\ keyword\ to\ identify\ the\ search"]
#     page.locator("[placeholder=\"Select\\ the\\ property\\ search\\,\\ or\\ enter\\ a\\ keyword\\ to\\ identify\\ the\\ search\"]").fill(admin_new_productname)
#     # Click text=CreateAdvanced Search >> button >> nth=1
#     page.locator("text=CreateAdvanced Search >> button").nth(1).click()
#     # Click text=productname1234567890
#     page.locator("text="+admin_new_productname).click()    
#     content = page.text_content("text="+admin_new_productname)
#     assert content == str(admin_new_productname)

# def test_puton_product(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
#     product_admin.PutonProduct(page, admin_productname)
#     # Go to https://admin-banana-dev.chunsutech.com/commodity/list
#     page.goto("https://admin-banana-dev.chunsutech.com/commodity/list")
#     # Click [placeholder="Select\ the\ property\ search\,\ or\ enter\ a\ keyword\ to\ identify\ the\ search"]
#     page.locator("[placeholder=\"Select\\ the\\ property\\ search\\,\\ or\\ enter\\ a\\ keyword\\ to\\ identify\\ the\\ search\"]").click()
#     # Fill [placeholder="Select\ the\ property\ search\,\ or\ enter\ a\ keyword\ to\ identify\ the\ search"]
#     page.locator("[placeholder=\"Select\\ the\\ property\\ search\\,\\ or\\ enter\\ a\\ keyword\\ to\\ identify\\ the\\ search\"]").fill(admin_productname)
#     # Click text=CreateAdvanced Search >> button >> nth=1
#     page.locator("text=CreateAdvanced Search >> button").nth(1).click()
#     # Click [aria-label="reload"] svg
#     page.locator("[aria-label=\"reload\"] svg").click()
#     # Click tbody >> text=Live
#     page.locator("td:nth-child(8)").first.click()
#     content = page.text_content("td:nth-child(8)")
#     # print(f'content:{content}')
#     assert content == "Live"

# def test_putoff_product(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
#     product_admin.PutoffProduct(page, admin_productname)
#     # Go to https://admin-banana-dev.chunsutech.com/commodity/list
#     page.goto("https://admin-banana-dev.chunsutech.com/commodity/list")
#     # Click [placeholder="Select\ the\ property\ search\,\ or\ enter\ a\ keyword\ to\ identify\ the\ search"]
#     page.locator("[placeholder=\"Select\\ the\\ property\\ search\\,\\ or\\ enter\\ a\\ keyword\\ to\\ identify\\ the\\ search\"]").click()
#     # Fill [placeholder="Select\ the\ property\ search\,\ or\ enter\ a\ keyword\ to\ identify\ the\ search"]
#     page.locator("[placeholder=\"Select\\ the\\ property\\ search\\,\\ or\\ enter\\ a\\ keyword\\ to\\ identify\\ the\\ search\"]").fill(admin_productname)
#     # Click text=CreateAdvanced Search >> button >> nth=1
#     page.locator("text=CreateAdvanced Search >> button").nth(1).click()
#     # Click [aria-label="reload"] svg
#     page.locator("[aria-label=\"reload\"] svg").click()
#     # Click tbody >> text=Live
#     page.locator("td:nth-child(8)").first.click()
#     content = page.text_content("td:nth-child(8)")
#     # print(f'content:{content}')
#     assert content == "Delisted"

# def test_set_product_category(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
#     product_admin.SetProductCategory(page, admin_productname)
#     # Click .ant-message-notice-content
#     page.locator(".ant-message-notice-content").click()
#     content = page.text_content(".ant-message-notice-content")
#     assert content == "设置分组成功!"

# def test_set_prduct_freightunified(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
#     product_admin.SetProductFreightunified(page, admin_productname)
#     # Click .ant-message-notice-content
#     page.locator(".ant-message-notice-content").click()
#     content = page.text_content(".ant-message-notice-content")
#     assert content == "设置统一运费成功!"

def test_set_product_freighttemplate(page):
    login_admin.AdminLogin(page,admin_username,admin_password)
    product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
    product_admin.SetProductFreighttemplate(page, admin_productname)
    # Click .ant-message-notice-content
    page.locator(".ant-message-notice-content").click()
    content = page.text_content(".ant-message-notice-content")
    assert content == "设置运费模版成功!"