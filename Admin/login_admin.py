
def AdminLogin(page, admin_username, admin_password):
    
    # Go to https://admin-banana-dev.chunsutech.com/user/login
    page.goto("https://admin-banana-dev.chunsutech.com/user/login")
    # Click [placeholder="Please\ enter\ username"]
    page.locator("[placeholder=\"Please\\ enter\\ username\"]").click()
    # Fill [placeholder="Please\ enter\ username"]
    page.locator("[placeholder=\"Please\\ enter\\ username\"]").fill(admin_username)
    # Fill [placeholder="Please\ enter\ password"]
    page.locator("[placeholder=\"Please\\ enter\\ password\"]").fill(admin_password)
    # Click button:has-text("Submit")
    # with page.expect_navigation(url="https://admin-banana-dev.chunsutech.com/dashboard"):
    with page.expect_navigation():
        page.locator("button:has-text(\"Submit\")").click()
    
def AdminLogout(page):
     # Go to https://admin-banana-dev.chunsutech.com/dashboard
    page.goto("https://admin-banana-dev.chunsutech.com/dashboard")
    # Click [aria-label="down"] svg
    page.locator("[aria-label=\"down\"] svg").hover()
    # Click text=Logout
    # with page.expect_navigation(url="https://admin-banana-dev.chunsutech.com/user/login"):
    with page.expect_navigation():
        page.locator("text=Logout").click()