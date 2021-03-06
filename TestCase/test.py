from Admin import login_admin, roles_admin, user_admin, category_admin, product_admin, resources_admin, order_admin, shipment_admin, finance_admin, tools_admin
from Client import login_client, search_client, buy_client, address_client, order_client
from API import change_order_status
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
#     assert content == "Delete Success!"#    ????????????

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
#     assert content == "??????????????????!"

# def test_set_prduct_freightunified(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
#     product_admin.SetProductFreightunified(page, admin_productname)
#     # Click .ant-message-notice-content
#     page.locator(".ant-message-notice-content").click()
#     content = page.text_content(".ant-message-notice-content")
#     assert content == "????????????????????????!"

# def test_set_product_freighttemplate(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
#     product_admin.SetProductFreighttemplate(page, admin_productname)
#     # Click .ant-message-notice-content
#     page.locator(".ant-message-notice-content").click()
#     content = page.text_content(".ant-message-notice-content")
#     assert content == "????????????????????????!"

# def test_set_product_shipment(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
#     product_admin.SetProductShipment(page, admin_productname)
#     # Click .ant-message-notice-content
#     page.locator(".ant-message-notice-content").click()
#     content = page.text_content(".ant-message-notice-content")
#     assert content == "?????????????????????!"

# def test_delete_product(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
#     product_admin.DeleteProduct(page, admin_productname)
#     # Click .ant-message-notice-content
#     page.locator(".ant-message-notice-content").click()
#     content = page.text_content(".ant-message-notice-content")
#     assert content == "????????????!"

admin_groupname = "Group"+str(int(time.time()))

# def test_add_group(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     resources_admin.AddGroup(page, admin_groupname)
#     # Click .ant-message-notice-content
#     page.locator(".ant-message-notice-content").click()
#     content = page.text_content(".ant-message-notice-content")
#     assert content == "Create Group Success!"

# def test_add_subgroup(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     resources_admin.AddGroup(page, admin_groupname)
#     admin_subgroupname = "Sub_"+admin_groupname
#     resources_admin.AddSubgroup(page, admin_groupname, admin_subgroupname)
#     # Click .ant-message-notice-content
#     page.locator(".ant-message-notice-content").click()
#     content = page.text_content(".ant-message-notice-content")
#     assert content == "Create Group Success!"

# def test_change_group(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     resources_admin.AddGroup(page, admin_groupname)
#     admin_new_groupname = "Change"+str(int(time.time()))
#     resources_admin.ChangeGroup(page, admin_groupname, admin_new_groupname)
#     # Click .ant-message-notice-content
#     page.locator(".ant-message-notice-content").click()
#     content = page.text_content(".ant-message-notice-content")
#     assert content == "Change Group Success!"
    
# def test_change_subgroup(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     resources_admin.AddGroup(page, admin_groupname)
#     admin_subgroupname = "Sub_"+admin_groupname
#     resources_admin.AddSubgroup(page, admin_groupname, admin_subgroupname)
#     admin_new_subgroupname = "ChangeSub"+str(int(time.time()))
#     resources_admin.ChangeSubgroup(page, admin_subgroupname, admin_new_subgroupname)
#     # Click .ant-message-notice-content
#     page.locator(".ant-message-notice-content").click()
#     content = page.text_content(".ant-message-notice-content")
#     assert content == "Change Group Success!"

# def test_delete_subgroup(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     resources_admin.AddGroup(page, admin_groupname)
#     admin_subgroupname = "Sub_"+admin_groupname
#     resources_admin.AddSubgroup(page, admin_groupname, admin_subgroupname)
#     resources_admin.DeleteSubgroup(page, admin_subgroupname)
#     # Click .ant-message-notice-content
#     page.locator(".ant-message-notice-content").click()
#     content = page.text_content(".ant-message-notice-content")
#     assert content == "Delete Group Success!"

# def test_delete_group(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     resources_admin.AddGroup(page, admin_groupname)
#     resources_admin.DeleteGroup(page, admin_groupname)
#     # Click .ant-message-notice-content
#     page.locator(".ant-message-notice-content").click()
#     content = page.text_content(".ant-message-notice-content")
#     assert content == "Delete Group Success!"

# def test_add_image(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     resources_admin.AddGroup(page, admin_groupname)
#     resources_admin.AddImage(page, admin_groupname)
#     page.locator(".ant-message-notice-content").click()
#     content = page.text_content(".ant-message-notice-content")
#     assert content == "Add Image Success!"

# def test_change_imagegroup(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     resources_admin.AddGroup(page, admin_groupname)
#     resources_admin.AddImage(page, admin_groupname)
#     resources_admin.ChangeImageGroup(page, admin_groupname)
#     page.locator(".ant-message-notice-content").click()
#     content = page.text_content(".ant-message-notice-content")
#     assert content == "Change Group Success!"

# def test_delete_image(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     resources_admin.AddGroup(page, admin_groupname)
#     resources_admin.AddImage(page, admin_groupname)
#     resources_admin.DeleteImage(page, admin_groupname)
#     page.locator(".ant-message-notice-content").click()
#     content = page.text_content(".ant-message-notice-content")
#     assert content == "Delete Success!"

customer_phone = "8615195927818"
customer_password = "qwer`123"

fullname = "Edison Cheung"
phonenumber = customer_phone
zipcode = str(int(time.time()))
detail = "Test_detail"

# def test_scene_buy(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
#     login_client.ClientLogin(page, customer_phone, customer_password)
#     address_client.AddAddress(page, fullname, phonenumber, zipcode, detail)
#     search_client.SearchProduct(page, admin_productname)
#     buy_client.BuyProduct(page)
#     content = page.text_content("text=field Signature is not set")
#     assert str(content) == "field Signature is not set"


headers = {'Authorization': '4211278B73B3424AB9B6701C83B558F5', 'X-Tenant-Type':'client'}

# def test_scene_payment(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
#     login_client.ClientLogin(page, customer_phone, customer_password)
#     address_client.AddAddress(page, fullname, phonenumber, zipcode, detail)
#     search_client.SearchProduct(page, admin_productname)
#     buy_client.BuyProduct(page)
#     order_id = order_client.GetOrderId(page, admin_productname)
#     order_status = change_order_status.ipay88Complete(payment_number=order_id, headers=headers)
#     assert str(order_status.status_code) == "200"

# def test_cart_product(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
#     login_client.ClientLogin(page, customer_phone, customer_password)
#     search_client.SearchProduct(page, admin_productname)
#     buy_client.CartProduct(page)
#     content = page.text_content("div > div > div.MuiAlert-message.css-1w0ym84")
#     assert str(content) == "Add to cart successfully"

# def test_checkout_cart(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
#     login_client.ClientLogin(page, customer_phone, customer_password)
#     address_client.AddAddress(page, fullname, phonenumber, zipcode, detail)
#     search_client.SearchProduct(page, admin_productname)
#     buy_client.CartProduct(page)
#     buy_client.CheckoutCart(page)
#     content = page.text_content("text=field Signature is not set")
#     assert str(content) == "field Signature is not set\n

# def test_cancel_order(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
#     login_client.ClientLogin(page, customer_phone, customer_password)
#     address_client.AddAddress(page, fullname, phonenumber, zipcode, detail)
#     search_client.SearchProduct(page, admin_productname)
#     buy_client.BuyProduct(page)
#     order_id = order_client.GetOrderId(page, admin_productname)
#     order_client.CancelUnpaidOrder(page, order_id)
#     content = page.text_content("#root-box > div.h-44px.flex.justify-around.items-center.px-2.bg-white > div.flex-1.text-normal.text-xxl.text-center.flex.flex-col")
#     assert str(content) == "Canceled"

# def test_paynow_order(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
#     login_client.ClientLogin(page, customer_phone, customer_password)
#     address_client.AddAddress(page, fullname, phonenumber, zipcode, detail)
#     search_client.SearchProduct(page, admin_productname)
#     buy_client.BuyProduct(page)
#     order_id = order_client.GetOrderId(page, admin_productname)
#     order_client.PaynowUnpaidOrder(page, order_id)
#     content = page.text_content("html")
#     assert str(content) == "field Signature is not set\n"

# def test_return_order(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
#     login_client.ClientLogin(page, customer_phone, customer_password)
#     address_client.AddAddress(page, fullname, phonenumber, zipcode, detail)
#     search_client.SearchProduct(page, admin_productname)
#     buy_client.BuyProduct(page)
#     order_id = order_client.GetOrderId(page, admin_productname)
#     change_order_status.ipay88Complete(payment_number=order_id, headers=headers)
#     return_description = "Return"+str(int(time.time()))
#     order_client.ReturnShipOrder(page, order_id, return_description)
#     order_admin.SearchReturnOrder(page, order_id)
#     content = page.text_content("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div > div.ant-col.ant-col-16 > div.detailDescription___Lrvi9 > div.detailIds___b3ust > div:nth-child(2) > div:nth-child(2)")
#     assert str(content) == str(order_id)

# def test_refund_order(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
#     login_client.ClientLogin(page, customer_phone, customer_password)
#     address_client.AddAddress(page, fullname, phonenumber, zipcode, detail)
#     search_client.SearchProduct(page, admin_productname)
#     buy_client.BuyProduct(page)
#     order_id = order_client.GetOrderId(page, admin_productname)
#     change_order_status.ipay88Complete(payment_number=order_id, headers=headers)
#     refund_description = "Refund"+str(int(time.time()))
#     order_client.RefundShipOrder(page, order_id, refund_description)
#     order_admin.SearchReturnOrder(page, order_id)
#     content = page.text_content("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div > div.ant-col.ant-col-16 > div.detailDescription___Lrvi9 > div.detailIds___b3ust > div:nth-child(2) > div:nth-child(2)")
#     assert str(content) == str(order_id)

# def test_return_refund_order(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
#     login_client.ClientLogin(page, customer_phone, customer_password)
#     address_client.AddAddress(page, fullname, phonenumber, zipcode, detail)
#     search_client.SearchProduct(page, admin_productname)
#     buy_client.BuyProduct(page)
#     order_id = order_client.GetOrderId(page, admin_productname)
#     change_order_status.ipay88Complete(payment_number=order_id, headers=headers)
#     returnrefund_description = "Return&Refund"+str(int(time.time()))
#     order_client.ReturnRefundShipOrder(page, order_id, returnrefund_description)
#     order_admin.SearchReturnOrder(page, order_id)
#     content = page.text_content("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div > div.ant-col.ant-col-16 > div.detailDescription___Lrvi9 > div.detailIds___b3ust > div:nth-child(2) > div:nth-child(2)")
#     assert str(content) == str(order_id)

# def test_agree_return_order(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
#     login_client.ClientLogin(page, customer_phone, customer_password)
#     address_client.AddAddress(page, fullname, phonenumber, zipcode, detail)
#     search_client.SearchProduct(page, admin_productname)
#     buy_client.BuyProduct(page)
#     order_id = order_client.GetOrderId(page, admin_productname)
#     change_order_status.ipay88Complete(payment_number=order_id, headers=headers)
#     return_description = "Return"+str(int(time.time()))
#     order_client.ReturnShipOrder(page, order_id, return_description)
#     order_admin.AgreeReturnOrder(page, order_id)
#     content = page.text_content("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div > div.ant-col.ant-col-16 > div.top___1xk1t > div.topName___qj6_B")
#     assert str(content) == "To Respond"

# def test_agree_return_order(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
#     login_client.ClientLogin(page, customer_phone, customer_password)
#     address_client.AddAddress(page, fullname, phonenumber, zipcode, detail)
#     search_client.SearchProduct(page, admin_productname)
#     buy_client.BuyProduct(page)
#     order_id = order_client.GetOrderId(page, admin_productname)
#     change_order_status.ipay88Complete(payment_number=order_id, headers=headers)
#     return_description = "Return"+str(int(time.time()))
#     order_client.ReturnShipOrder(page, order_id, return_description)
#     reject_reson = "Reject"+str(int(time.time()))
#     order_admin.RejectReturnOrder(page, order_id, reject_reson)
#     content = page.text_content("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div > div.ant-col.ant-col-16 > div.top___1xk1t > div.topName___qj6_B")
#     assert str(content) == "Request Cancelled"

# def test_confirm_receipt_return_order(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
#     login_client.ClientLogin(page, customer_phone, customer_password)
#     address_client.AddAddress(page, fullname, phonenumber, zipcode, detail)
#     search_client.SearchProduct(page, admin_productname)
#     buy_client.BuyProduct(page)
#     order_id = order_client.GetOrderId(page, admin_productname)
#     change_order_status.ipay88Complete(payment_number=order_id, headers=headers)
#     return_description = "Return"+str(int(time.time()))
#     order_client.ReturnShipOrder(page, order_id, return_description)
#     order_admin.AgreeReturnOrder(page, order_id)
#     order_admin.ConfirmReceiptRetunOrder(page, order_id)
#     content = page.text_content("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div > div.ant-col.ant-col-16 > div.top___1xk1t > div.topName___qj6_B")
#     assert str(content) == "Request Completed"

# def test_cancel_receipt_return_order(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
#     login_client.ClientLogin(page, customer_phone, customer_password)
#     address_client.AddAddress(page, fullname, phonenumber, zipcode, detail)
#     search_client.SearchProduct(page, admin_productname)
#     buy_client.BuyProduct(page)
#     order_id = order_client.GetOrderId(page, admin_productname)
#     change_order_status.ipay88Complete(payment_number=order_id, headers=headers)
#     return_description = "Return"+str(int(time.time()))
#     order_client.ReturnShipOrder(page, order_id, return_description)
#     print(f'\norder_id:{order_id}')
#     order_admin.AgreeReturnOrder(page, order_id)
#     cancel_reson = "Cancel"+str(int(time.time()))
#     order_admin.CancelReceiptRetunOrder(page, order_id, cancel_reson)
#     content = page.text_content("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div > div.ant-col.ant-col-16 > div.top___1xk1t > div.topName___qj6_B")
#     assert str(content) == "Request Cancelled"

# def test_arrange_shipment(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
#     login_client.ClientLogin(page, customer_phone, customer_password)
#     address_client.AddAddress(page, fullname, phonenumber, zipcode, detail)
#     search_client.SearchProduct(page, admin_productname)
#     buy_client.BuyProduct(page)
#     order_id = order_client.GetOrderId(page, admin_productname)
#     change_order_status.ipay88Complete(payment_number=order_id, headers=headers)
#     ship_company_id = "ShipCo"+str(int(time.time()))
#     ship_no = str(int(time.time()))
#     order_admin.ArrageShipment(page, order_id, ship_company_id, ship_no)
#     content = page.text_content(".ant-message-custom-content")
#     assert str(content) == "Arrange Shipment Success!"

# def test_delivery_confirmed(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
#     login_client.ClientLogin(page, customer_phone, customer_password)
#     address_client.AddAddress(page, fullname, phonenumber, zipcode, detail)
#     search_client.SearchProduct(page, admin_productname)
#     buy_client.BuyProduct(page)
#     order_id = order_client.GetOrderId(page, admin_productname)
#     change_order_status.ipay88Complete(payment_number=order_id, headers=headers)
#     ship_company_id = "ShipCo"+str(int(time.time()))
#     ship_no = str(int(time.time()))
#     order_admin.ArrageShipment(page, order_id, ship_company_id, ship_no)
#     order_client.DeliveryConfirmed(page, order_id)
#     content = page.text_content(".h-44px")
#     assert str(content) == "Completed"

# def test_change_order_total(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
#     login_client.ClientLogin(page, customer_phone, customer_password)
#     address_client.AddAddress(page, fullname, phonenumber, zipcode, detail)
#     search_client.SearchProduct(page, admin_productname)
#     buy_client.BuyProduct(page)
#     order_id = order_client.GetOrderId(page, admin_productname)
#     total_price = "100"
#     ship_price = "50"
#     order_admin.ChangeOrderTotal(page, order_id, total_price, ship_price)
#     content = page.text_content(".ant-message-notice-content")
#     assert str(content) == "Change Price Success!"

module_name_pkg = "PKG"+str(int(time.time()))
first_piece = "1"
freight = "1"
continuation = "1"
rnenw = "1"

# def test_create_delivery_pkg(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     module_name=module_name_pkg
#     shipment_admin.CreateDeliveryPKG(page, module_name, first_piece, freight, continuation, rnenw)
#     shipment_admin.SearchDelivery(page, module_name)
#     content = page.text_content("text="+module_name)
#     assert str(content) != str(module_name)

module_name_weight = "Weight"+str(int(time.time()))
first_weight = "1"
continued_weight = "1"

# def test_create_delivery_weight(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     module_name = module_name_weight
#     shipment_admin.CreateDeliveryWeight(page, module_name, first_weight, freight, continued_weight, rnenw)
#     shipment_admin.SearchDelivery(page, module_name)
#     content = page.text_content("text="+module_name)
#     assert str(content) != str(module_name)

# def test_edit_delivery(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     module_name=module_name_pkg
#     shipment_admin.CreateDeliveryPKG(page, module_name, first_piece, freight, continuation, rnenw)
#     shipment_admin.SearchDelivery(page, module_name)
#     module_change_name = "Change_"+module_name
#     shipment_admin.EditDelivery(page, module_change_name)
#     shipment_admin.SearchDelivery(page, module_change_name)
#     content = page.text_content("text="+module_change_name)
#     assert str(content) != str(module_change_name)

# def test_delete_delivery(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     module_name=module_name_pkg
#     shipment_admin.CreateDeliveryPKG(page, module_name, first_piece, freight, continuation, rnenw)
#     shipment_admin.SearchDelivery(page, module_name)
#     shipment_admin.DeleteDelivery(page)
#     content = page.text_content(".ant-message-notice-content")
#     assert str(content) == "Delete Template Success!"

# def test_modify_calculatefee(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     shipment_admin.ModifyCalculateFee(page)

# def test_completed_topay(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
#     login_client.ClientLogin(page, customer_phone, customer_password)
#     address_client.AddAddress(page, fullname, phonenumber, zipcode, detail)
#     search_client.SearchProduct(page, admin_productname)
#     buy_client.BuyProduct(page)
#     order_id = order_client.GetOrderId(page, admin_productname)
#     change_order_status.ipay88Complete(payment_number=order_id, headers=headers)
#     return_description = "Return"+str(int(time.time()))
#     order_client.ReturnShipOrder(page, order_id, return_description)
#     order_admin.AgreeReturnOrder(page, order_id)
#     order_admin.ConfirmReceiptRetunOrder(page, order_id)
#     return_id = order_admin.GetReturnId(page, order_id)
#     actual_amount = "100"
#     # print(f'\norder_id:{order_id}')
#     # print(f'\nreturn_id:{return_id}')
#     finance_admin.CompletedToPay(page,return_id,actual_amount)
#     content = page.text_content("td:nth-child(5)")
#     assert str(content) == "completed"

voucher_name_percent = "Percent"+str(int(time.time()))
voucher_name_amount = "Amount"+str(int(time.time()))
voucher_code = "A"+str(random.randint(0,9999))
amount = "10" 
usage_quantity = "1"
min_price = "1"

# def test_create_voucher_percentage(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     voucher_name = voucher_name_percent
#     tools_admin.CreateVoucherPercentage(page,voucher_name, voucher_code, amount, usage_quantity,min_price)
#     content = page.text_content(".ant-message-notice-content")
#     assert str(content) == "Create Success!"

# def test_create_voucher_amount(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     voucher_name = voucher_name_amount
#     tools_admin.CreateVoucherAmount(page,voucher_name, voucher_code, amount, usage_quantity,min_price)
#     content = page.text_content(".ant-message-notice-content")
#     assert str(content) == "Create Success!"

# def  test_delete_voucher(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     voucher_name = voucher_name_percent
#     tools_admin.CreateVoucherPercentage(page,voucher_name, voucher_code, amount, usage_quantity,min_price)
#     tools_admin.DeleteVoucher(page)
#     content = page.text_content(".ant-table-container > div > table > tbody > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1)")
#     assert str(content) != str(voucher_code)

# def test_buy_with_voucher(page):
#     login_admin.AdminLogin(page,admin_username,admin_password)
#     product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
#     voucher_name = voucher_name_percent
#     tools_admin.CreateVoucherPercentage(page,voucher_name, voucher_code, amount, usage_quantity,min_price)
#     login_client.ClientLogin(page, customer_phone, customer_password)
#     address_client.AddAddress(page, fullname, phonenumber, zipcode, detail)
#     search_client.SearchProduct(page, admin_productname)
#     buy_client.BuyWithVoucher(page, voucher_code)
#     content = page.text_content("text=field Signature is not set")
#     assert str(content) == "field Signature is not set\n"
