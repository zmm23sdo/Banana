from Admin import login, product
import random

username = "mingvtest2"
password = "qwer`123"
Random = str(random.randint(0,99999))
product_name = "test_product_name_000"+Random
def test_create_product(page):
    login.login(page, username, password)
    product.create_group(page)
    product.create_prouct(page,product_name)
    with page.expect_navigation():
        # Go to https://admin-banana-test.chunsutech.com/commodity/list https://admin-banana-test.chunsutech.com/commodity/list
        # page.goto("https://admin-banana-test.chunsutech.com/commodity/list")
        # Click [aria-label="reload"] svg
        page.locator("[aria-label=\"reload\"] svg").click()
    page.locator("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div:nth-child(3) > div > div > div > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div > div > div:nth-child(1)").click()
    content = page.text_content('#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div:nth-child(3) > div > div > div > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div > div > div:nth-child(1)')
                                    #root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div:nth-child(3) > div > div > div > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div > div > div:nth-child(1)
    
    
    print(f'\ncontent = {content}' )
    print(f'Product Name : {product_name}')
    assert content == product_name