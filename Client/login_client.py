def ClientLogin(page, customer_phone, customer_password):
    # Go to https://client-banana-dev.chunsutech.com/home
    page.goto("https://client-banana-dev.chunsutech.com/home")
    # Click button:has-text("Me")
    # with page.expect_navigation(url="https://client-banana-dev.chunsutech.com/management"):
    with page.expect_navigation():
        page.locator("button:has-text(\"Me\")").click()
    # Click text=Login/Register Now!
    # with page.expect_navigation(url="https://client-banana-dev.chunsutech.com/user?redirection=%2Fmanagement"):
    with page.expect_navigation():
        page.locator("text=Login/Register Now!").click()
    # Click input[name="phoneNumber"]
    page.locator("input[name=\"phoneNumber\"]").click()
    # Fill input[name="phoneNumber"]
    page.locator("input[name=\"phoneNumber\"]").fill(customer_phone)
    # Click text=Phone NumberPassword >> div >> nth=2
    page.locator("text=Phone NumberPassword >> div").nth(2).click()
    # Fill input[name="password"]
    page.locator("input[name=\"password\"]").fill(customer_password)
    # Click text=Submit
    # with page.expect_navigation(url="https://client-banana-dev.chunsutech.com/management"):
    with page.expect_navigation():
        page.locator("text=Submit").click()
