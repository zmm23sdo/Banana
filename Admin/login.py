

def login(page,username,password):

    # Go to https://admin-banana-test.chunsutech.com/
    page.goto("https://admin-banana-test.chunsutech.com/")
    # Go to https://admin-banana-test.chunsutech.com/user/login
    page.goto("https://admin-banana-test.chunsutech.com/user/login")
    # Fill [placeholder="Username\:\ admin\ or\ user"]
    page.locator("[placeholder=\"Username\\:\\ admin\\ or\\ user\"]").fill(username)
    # Press Tab
    page.locator("[placeholder=\"Username\\:\\ admin\\ or\\ user\"]").press("Tab")
    # Fill [placeholder="Password\:\ ant\.design"]
    page.locator("[placeholder=\"Password\\:\\ ant\\.design\"]").fill(password)
    # Press Enter
    # with page.expect_navigation(url="https://admin-banana-test.chunsutech.com/dashboard"):
    with page.expect_navigation():
        page.locator("[placeholder=\"Password\\:\\ ant\\.design\"]").press("Enter")
