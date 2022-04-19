def AddAddress(page, fullname, phonenumber, zipcode, detail):
    # Go to https://client-banana-dev.chunsutech.com/home
    page.goto("https://client-banana-dev.chunsutech.com/home")
    # Click button:has-text("Me")
    # with page.expect_navigation(url="https://client-banana-dev.chunsutech.com/management"):
    with page.expect_navigation():
        page.locator("button:has-text(\"Me\")").click()
    # Click text=Account Setting >
    # with page.expect_navigation(url="https://client-banana-dev.chunsutech.com/management/account"):
    with page.expect_navigation():
        page.locator("text=Account Setting >").click()
    # Click text=Address Booking >
    # with page.expect_navigation(url="https://client-banana-dev.chunsutech.com/management/account/address"):
    with page.expect_navigation():
        page.locator("text=Address Booking >").click()
    # Click #root-box div:has-text("Add Address") >> nth=1
    page.locator("#root-box div:has-text(\"Add Address\")").nth(1).click()
    # Fill [placeholder="Please\ enter"] >> nth=0
    page.locator("[placeholder=\"Please\\ enter\"]").first.fill(fullname)
    # Fill [placeholder="Please\ enter"] >> nth=1
    page.locator("[placeholder=\"Please\\ enter\"]").nth(1).fill(phonenumber)
    # Click text=Area, StatePlease select>
    page.locator("text=Area, StatePlease select>").click()
    # Click text=Terengganu
    page.locator("text=Terengganu").click()
    # Click text=Ajil
    page.locator("text=Ajil").click()
    # Fill [placeholder="Please\ enter"] >> nth=2
    page.locator("[placeholder=\"Please\\ enter\"]").nth(2).fill(zipcode)
    # Fill [placeholder="Please\ enter"] >> nth=3
    page.locator("[placeholder=\"Please\\ enter\"]").nth(3).fill(detail)
    # Check input[type="checkbox"]
    page.locator("input[type=\"checkbox\"]").check()
    # Click #root-box div:has-text("Submit") >> nth=1
    # with page.expect_navigation(url="https://client-banana-dev.chunsutech.com/management/account/address"):
    with page.expect_navigation():
        page.locator("#root-box div:has-text(\"Submit\")").nth(1).click()