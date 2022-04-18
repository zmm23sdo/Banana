def BuyProduct(page):
    page.locator(".absolute img").first.click()
    # Click text=WishAdd To CartBuy Now
    page.locator("text=WishAdd To CartBuy Now").click()
    # Click text=Buy Now
    page.locator("text=Buy Now").click()
    # Click text=General
    page.locator("text=General").click()
    # Click #select_drawer div:has-text("Buy Now") >> nth=2
    page.locator("#select_drawer div:has-text(\"Buy Now\")").nth(2).click()