def CreateUser(page, admin_new_username, admin_new_fullname, admin_new_email, admin_new_password):
    # Go to https://admin-banana-test.chunsutech.com/users/users
    page.goto("https://admin-banana-test.chunsutech.com/users/users")
    # Click button:has-text("Create User")
    page.locator("button:has-text(\"Create User\")").click()
    # Fill [placeholder="\35 -15\ alphabets\ or\ numbers"]
    page.locator("[placeholder=\"\\35 -15\\ alphabets\\ or\\ numbers\"]").fill(admin_new_username)
    # Fill text=Fullname0 / 32 >> [placeholder="请输入"]
    page.locator("text=Fullname0 / 32 >> [placeholder=\"请输入\"]").fill(admin_new_fullname)
    # Fill #email
    page.locator("#email").fill(admin_new_email)
    # Click .ant-select-selection-overflow
    page.locator(".ant-select-selection-overflow").click()
    # Click text=AllAuth
    page.locator("text=AllAuth").click()
    # Fill input[type="password"]
    page.locator("input[type=\"password\"]").fill(admin_new_password)
    # Click button:has-text("确 认")
    page.locator("button:has-text(\"确 认\")").click()
    # Click .ant-message-notice-content
    page.locator(".ant-message-notice-content").click()

def EditUser(page, admin_new_username, admin_new_email):
    # Go to https://admin-banana-test.chunsutech.com/users/users/
    page.goto("https://admin-banana-test.chunsutech.com/users/users/")
    # Fill [placeholder="Select\ the\ property\ search\,\ or\ enter\ a\ keyword\ to\ identify\ the\ search"]
    page.locator("[placeholder=\"Select\\ the\\ property\\ search\\,\\ or\\ enter\\ a\\ keyword\\ to\\ identify\\ the\\ search\"]").fill(admin_new_username)
    # Click text=Create UserAdvanced Search >> button >> nth=1
    page.locator("text=Create UserAdvanced Search >> button").nth(1).click()
    # Click [aria-label="reload"] svg
    page.locator("[aria-label=\"reload\"] svg").click()
    # Click button:has-text("Edit") >> nth=0
    page.locator("button:has-text(\"Edit\")").first.click()
    # Fill text=Fullname0 / 32 >> [placeholder="请输入"]
    page.locator("#name").fill("Change "+admin_new_username)
    # Fill #email
    page.locator("#email").fill(admin_new_email+"co")
    # Click button:has-text("确 认")
    page.locator("button:has-text(\"确 认\")").click()
    # Click .ant-message-notice-content
    page.locator(".ant-message-notice-content").click()

def DeleteUser(page,admin_new_username):
    # Go to https://admin-banana-test.chunsutech.com/users/users/
    page.goto("https://admin-banana-test.chunsutech.com/users/users/")
    # Fill [placeholder="Select\ the\ property\ search\,\ or\ enter\ a\ keyword\ to\ identify\ the\ search"]
    page.locator("[placeholder=\"Select\\ the\\ property\\ search\\,\\ or\\ enter\\ a\\ keyword\\ to\\ identify\\ the\\ search\"]").fill(admin_new_username)
    # Click text=Create UserAdvanced Search >> button >> nth=1
    page.locator("text=Create UserAdvanced Search >> button").nth(1).click()
    # Click [aria-label="reload"] svg
    page.locator("[aria-label=\"reload\"] svg").click()
    # Click button:has-text("Delete") >> nth=0
    page.locator("button:has-text(\"Delete\")").first.click()
    # Click button:has-text("Confirm")
    page.locator("button:has-text(\"Confirm\")").click()
    # Click .ant-message-notice-content
    page.locator(".ant-message-notice-content").click()