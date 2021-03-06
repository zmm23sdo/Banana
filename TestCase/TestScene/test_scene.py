from Admin import login_admin, product_admin, order_admin, finance_admin
from Client import login_client, search_client, buy_client, address_client, order_client
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


def test_scene_buy(page):
    login_admin.AdminLogin(page,admin_username,admin_password)
    product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
    login_client.ClientLogin(page, customer_phone, customer_password)
    address_client.AddAddress(page, fullname, phonenumber, zipcode, detail)
    search_client.SearchProduct(page, admin_productname)
    buy_client.BuyProduct(page)
    content = page.text_content("text=field Signature is not set")
    assert str(content) == "field Signature is not set"

headers = {'Authorization': '4211278B73B3424AB9B6701C83B558F5', 'X-Tenant-Type':'client'}

def test_scene_payment(page):
    login_admin.AdminLogin(page,admin_username,admin_password)
    product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
    login_client.ClientLogin(page, customer_phone, customer_password)
    address_client.AddAddress(page, fullname, phonenumber, zipcode, detail)
    search_client.SearchProduct(page, admin_productname)
    buy_client.BuyProduct(page)
    order_id = order_client.GetOrderId(page, admin_productname)
    order_status = change_order_status.ipay88Complete(payment_number=order_id, headers=headers)
    assert str(order_status.status_code) == "200"

def test_cart_product(page):
    login_admin.AdminLogin(page,admin_username,admin_password)
    product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
    login_client.ClientLogin(page, customer_phone, customer_password)
    search_client.SearchProduct(page, admin_productname)
    buy_client.CartProduct(page)
    content = page.text_content("div > div > div.MuiAlert-message.css-1w0ym84")
    assert str(content) == "Add to cart successfully"
    
def test_checkout_cart(page):
    login_admin.AdminLogin(page,admin_username,admin_password)
    product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
    login_client.ClientLogin(page, customer_phone, customer_password)
    address_client.AddAddress(page, fullname, phonenumber, zipcode, detail)
    search_client.SearchProduct(page, admin_productname)
    buy_client.CartProduct(page)
    buy_client.CheckoutCart(page)
    content = page.text_content("text=field Signature is not set")
    assert str(content) == "field Signature is not set\n"

def test_cancel_order(page):
    login_admin.AdminLogin(page,admin_username,admin_password)
    product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
    login_client.ClientLogin(page, customer_phone, customer_password)
    address_client.AddAddress(page, fullname, phonenumber, zipcode, detail)
    search_client.SearchProduct(page, admin_productname)
    buy_client.BuyProduct(page)
    order_id = order_client.GetOrderId(page, admin_productname)
    order_client.CancelUnpaidOrder(page, order_id)
    content = page.text_content("#root-box > div.h-44px.flex.justify-around.items-center.px-2.bg-white > div.flex-1.text-normal.text-xxl.text-center.flex.flex-col")
    assert str(content) == "Canceled"

def test_return_order(page):
    login_admin.AdminLogin(page,admin_username,admin_password)
    product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
    login_client.ClientLogin(page, customer_phone, customer_password)
    address_client.AddAddress(page, fullname, phonenumber, zipcode, detail)
    search_client.SearchProduct(page, admin_productname)
    buy_client.BuyProduct(page)
    order_id = order_client.GetOrderId(page, admin_productname)
    change_order_status.ipay88Complete(payment_number=order_id, headers=headers)
    return_description = "Return"+str(int(time.time()))
    order_client.ReturnShipOrder(page, order_id, return_description)
    order_admin.SearchReturnOrder(page, order_id)
    content = page.text_content("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div > div.ant-col.ant-col-16 > div.detailDescription___Lrvi9 > div.detailIds___b3ust > div:nth-child(2) > div:nth-child(2)")
    assert str(content) == str(order_id)

def test_refund_order(page):
    login_admin.AdminLogin(page,admin_username,admin_password)
    product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
    login_client.ClientLogin(page, customer_phone, customer_password)
    address_client.AddAddress(page, fullname, phonenumber, zipcode, detail)
    search_client.SearchProduct(page, admin_productname)
    buy_client.BuyProduct(page)
    order_id = order_client.GetOrderId(page, admin_productname)
    change_order_status.ipay88Complete(payment_number=order_id, headers=headers)
    refund_description = "Refund"+str(int(time.time()))
    order_client.RefundShipOrder(page, order_id, refund_description)
    order_admin.SearchReturnOrder(page, order_id)
    content = page.text_content("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div > div.ant-col.ant-col-16 > div.detailDescription___Lrvi9 > div.detailIds___b3ust > div:nth-child(2) > div:nth-child(2)")
    assert str(content) == str(order_id)

def test_return_refund_order(page):
    login_admin.AdminLogin(page,admin_username,admin_password)
    product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
    login_client.ClientLogin(page, customer_phone, customer_password)
    address_client.AddAddress(page, fullname, phonenumber, zipcode, detail)
    search_client.SearchProduct(page, admin_productname)
    buy_client.BuyProduct(page)
    order_id = order_client.GetOrderId(page, admin_productname)
    change_order_status.ipay88Complete(payment_number=order_id, headers=headers)
    returnrefund_description = "Return&Refund"+str(int(time.time()))
    order_client.ReturnRefundShipOrder(page, order_id, returnrefund_description)
    order_admin.SearchReturnOrder(page, order_id)
    content = page.text_content("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div > div.ant-col.ant-col-16 > div.detailDescription___Lrvi9 > div.detailIds___b3ust > div:nth-child(2) > div:nth-child(2)")
    assert str(content) == str(order_id)

def test_agree_return_order(page):
    login_admin.AdminLogin(page,admin_username,admin_password)
    product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
    login_client.ClientLogin(page, customer_phone, customer_password)
    address_client.AddAddress(page, fullname, phonenumber, zipcode, detail)
    search_client.SearchProduct(page, admin_productname)
    buy_client.BuyProduct(page)
    order_id = order_client.GetOrderId(page, admin_productname)
    change_order_status.ipay88Complete(payment_number=order_id, headers=headers)
    return_description = "Return"+str(int(time.time()))
    order_client.ReturnShipOrder(page, order_id, return_description)
    order_admin.AgreeReturnOrder(page, order_id)
    content = page.text_content("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div > div.ant-col.ant-col-16 > div.top___1xk1t > div.topName___qj6_B")
    assert str(content) == "To Respond"

def test_reject_return_order(page):
    login_admin.AdminLogin(page,admin_username,admin_password)
    product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
    login_client.ClientLogin(page, customer_phone, customer_password)
    address_client.AddAddress(page, fullname, phonenumber, zipcode, detail)
    search_client.SearchProduct(page, admin_productname)
    buy_client.BuyProduct(page)
    order_id = order_client.GetOrderId(page, admin_productname)
    change_order_status.ipay88Complete(payment_number=order_id, headers=headers)
    return_description = "Return"+str(int(time.time()))
    order_client.ReturnShipOrder(page, order_id, return_description)
    reject_reson = "Reject"+str(int(time.time()))
    order_admin.RejectReturnOrder(page, order_id, reject_reson)
    content = page.text_content("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div > div.ant-col.ant-col-16 > div.top___1xk1t > div.topName___qj6_B")
    assert str(content) == "Request Cancelled"

def test_confirm_receipt_return_order(page):
    login_admin.AdminLogin(page,admin_username,admin_password)
    product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
    login_client.ClientLogin(page, customer_phone, customer_password)
    address_client.AddAddress(page, fullname, phonenumber, zipcode, detail)
    search_client.SearchProduct(page, admin_productname)
    buy_client.BuyProduct(page)
    order_id = order_client.GetOrderId(page, admin_productname)
    change_order_status.ipay88Complete(payment_number=order_id, headers=headers)
    return_description = "Return"+str(int(time.time()))
    order_client.ReturnShipOrder(page, order_id, return_description)
    print(f'\norder_id:{order_id}')
    order_admin.AgreeReturnOrder(page, order_id)
    order_admin.ConfirmReceiptRetunOrder(page, order_id)
    content = page.text_content("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div > div.ant-col.ant-col-16 > div.top___1xk1t > div.topName___qj6_B")
    assert str(content) == "Request Completed"

def test_cancel_receipt_return_order(page):
    login_admin.AdminLogin(page,admin_username,admin_password)
    product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
    login_client.ClientLogin(page, customer_phone, customer_password)
    address_client.AddAddress(page, fullname, phonenumber, zipcode, detail)
    search_client.SearchProduct(page, admin_productname)
    buy_client.BuyProduct(page)
    order_id = order_client.GetOrderId(page, admin_productname)
    change_order_status.ipay88Complete(payment_number=order_id, headers=headers)
    return_description = "Return"+str(int(time.time()))
    order_client.ReturnShipOrder(page, order_id, return_description)
    print(f'\norder_id:{order_id}')
    order_admin.AgreeReturnOrder(page, order_id)
    cancel_reson = "Cancel"+str(int(time.time()))
    order_admin.CancelReceiptRetunOrder(page, order_id, cancel_reson)
    content = page.text_content("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div > div.ant-col.ant-col-16 > div.top___1xk1t > div.topName___qj6_B")
    assert str(content) == "Request Cancelled"

def test_arrange_shipment(page):
    login_admin.AdminLogin(page,admin_username,admin_password)
    product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
    login_client.ClientLogin(page, customer_phone, customer_password)
    address_client.AddAddress(page, fullname, phonenumber, zipcode, detail)
    search_client.SearchProduct(page, admin_productname)
    buy_client.BuyProduct(page)
    order_id = order_client.GetOrderId(page, admin_productname)
    change_order_status.ipay88Complete(payment_number=order_id, headers=headers)
    ship_company_id = "ShipCo"+str(int(time.time()))
    ship_no = str(int(time.time()))
    order_admin.ArrageShipment(page, order_id, ship_company_id, ship_no)
    content = page.text_content(".ant-message-custom-content")
    assert str(content) == "Arrange Shipment Success!"

def test_change_order_total(page):
    login_admin.AdminLogin(page,admin_username,admin_password)
    product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
    login_client.ClientLogin(page, customer_phone, customer_password)
    address_client.AddAddress(page, fullname, phonenumber, zipcode, detail)
    search_client.SearchProduct(page, admin_productname)
    buy_client.BuyProduct(page)
    order_id = order_client.GetOrderId(page, admin_productname)
    total_price = "100"
    ship_price = "50"
    order_admin.ChangeOrderTotal(page, order_id, total_price, ship_price)
    content = page.text_content(".ant-message-notice-content")
    assert str(content) == "Change Price Success!"

def test_completed_topay(page):
    login_admin.AdminLogin(page,admin_username,admin_password)
    product_admin.CreateProductBasic(page, admin_productname, admin_product_description, admin_product_price, admin_product_stock, admin_product_weight, admin_product_freight)
    login_client.ClientLogin(page, customer_phone, customer_password)
    address_client.AddAddress(page, fullname, phonenumber, zipcode, detail)
    search_client.SearchProduct(page, admin_productname)
    buy_client.BuyProduct(page)
    order_id = order_client.GetOrderId(page, admin_productname)
    change_order_status.ipay88Complete(payment_number=order_id, headers=headers)
    return_description = "Return"+str(int(time.time()))
    order_client.ReturnShipOrder(page, order_id, return_description)
    order_admin.AgreeReturnOrder(page, order_id)
    order_admin.ConfirmReceiptRetunOrder(page, order_id)
    return_id = order_admin.GetReturnId(page, order_id)
    actual_amount = "100"
    # print(f'\norder_id:{order_id}')
    # print(f'\nreturn_id:{return_id}')
    finance_admin.CompletedToPay(page,return_id,actual_amount)
    content = page.text_content("td:nth-child(5)")
    assert str(content) == "completed"