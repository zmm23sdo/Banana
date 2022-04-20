from Admin import login_admin, product_admin
from Client import login_client, search_client, buy_client, address_client
from API import change_order_status
import datetime
import random
import time

admin_username = "admin"
admin_password = "qwer@1234"

admin_productname = "Product"+str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
admin_product_description = "Product Description:\n\t"+admin_productname+"\n\t"+str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
admin_product_price = "300" 
admin_product_stock = "100" 
admin_product_weight = "1" 
admin_product_freight = "10"

customer_phone = "8615195927818"
customer_password = "qwer`123"

fullname = "Edison Cheung"
phonenumber = customer_phone
zipcode = str(int(time.time()))
detail = "Test_detail"
headers = {'Authorization': '4211278B73B3424AB9B6701C83B558F5', 'X-Tenant-Type':'client'}

def test_scene_buy(page):
    login_admin.AdminLogin(page,admin_username,admin_password)
    product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
    login_client.ClientLogin(page, customer_phone, customer_password)
    address_client.AddAddress(page, fullname, phonenumber, zipcode, detail)
    search_client.SearchProduct(page, admin_productname)
    buy_client.BuyProduct(page)
    content = page.text_content("text=field Signature is not set")
    assert str(content) == "field Signature is not set"
