from Client import buy

def test_buy(page):
    buy.buy_unlog(page)
    page.pause()

# def test_purchase():
