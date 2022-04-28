import imp
from Admin import login_admin, tools_admin
import time
import random

admin_username = "admin"
admin_password = "qwer@1234"

voucher_name_percent = "Percent"+str(int(time.time()))
voucher_name_amount = "Amount"+str(int(time.time()))
voucher_code = "A"+str(random.randint(0,9999))
amount = "10" 
usage_quantity = "1"
min_price = "1"

def test_create_voucher_percentage(page):
    login_admin.AdminLogin(page,admin_username,admin_password)
    voucher_name = voucher_name_percent
    tools_admin.CreateVoucherPercentage(page,voucher_name, voucher_code, amount, usage_quantity,min_price)
    content = page.text_content(".ant-message-notice-content")
    assert str(content) == "Create Success!"

def test_create_voucher_amount(page):
    login_admin.AdminLogin(page,admin_username,admin_password)
    voucher_name = voucher_name_amount
    tools_admin.CreateVoucherAmount(page,voucher_name, voucher_code, amount, usage_quantity,min_price)
    content = page.text_content(".ant-message-notice-content")
    assert str(content) == "Create Success!"

def  test_delete_voucher(page):
    login_admin.AdminLogin(page,admin_username,admin_password)
    voucher_name = voucher_name_percent
    tools_admin.CreateVoucherPercentage(page,voucher_name, voucher_code, amount, usage_quantity,min_price)
    tools_admin.DeleteVoucher(page)
    content = page.text_content(".ant-table-container > div > table > tbody > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1)")
    assert str(content) != str(voucher_code)