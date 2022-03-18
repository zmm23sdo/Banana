

def create_user(page, username, name, email, password):
    # Go to https://admin-banana-test.chunsutech.com/dashboard
    page.goto("https://admin-banana-test.chunsutech.com/dashboard")
    # Click span:has-text("Dashboard") >> nth=0
    page.locator("span:has-text(\"Dashboard\")").first.click()
    # Click span:has-text("User") >> nth=0
    page.locator("span:has-text(\"User\")").first.click()
    # Click a:has-text("Users")
    page.locator("a:has-text(\"Users\")").click()
    # assert page.url == "https://admin-banana-test.chunsutech.com/users/users"
    # Click button:has-text("Create User")
    page.locator("button:has-text(\"Create User\")").click()
    # Click [placeholder="\35 -15\ alphabets\ or\ numbers"]
    page.locator("[placeholder=\"\\35 -15\\ alphabets\\ or\\ numbers\"]").click()
    # Fill [placeholder="\35 -15\ alphabets\ or\ numbers"]
    page.locator("[placeholder=\"\\35 -15\\ alphabets\\ or\\ numbers\"]").fill(username)
    # Press Tab
    # page.locator("[placeholder=\"\\35 -15\\ alphabets\\ or\\ numbers\"]").press("Tab")
    # Fill text=Fullname0 / 32 >> [placeholder="请输入"]
    page.locator("text=Fullname0 / 32 >> [placeholder=\"请输入\"]").fill(name)
    # Click #email
    page.locator("#email").click()
    # Fill #email
    page.locator("#email").fill(email)
    # Click .ant-select-selection-overflow
    page.locator(".ant-select-selection-overflow").click()

    # Click .ant-select-item >> nth=0
    page.locator(".ant-select-item").first.click()

    # Click .ant-form div:nth-child(5) .ant-col.ant-form-item-label
    page.locator(".ant-form div:nth-child(5) .ant-col.ant-form-item-label").click()
    
    # Click input[type="password"]
    page.locator("input[type=\"password\"]").click()
    # Fill input[type="password"]
    page.locator("input[type=\"password\"]").fill(password)
    # Click button:has-text("确 认")
    page.locator("button:has-text(\"确 认\")").click()

def create_role(page, role_name, role_des):
    # Go to https://admin-banana-test.chunsutech.com/dashboard
    page.goto("https://admin-banana-test.chunsutech.com/dashboard")
    # Click span:has-text("Dashboard") >> nth=0
    page.locator("span:has-text(\"Dashboard\")").first.click()
    # Click span:has-text("User") >> nth=0
    page.locator("span:has-text(\"User\")").first.click()
    # Click a:has-text("Roles")
    page.locator("a:has-text(\"Roles\")").click()
    # assert page.url == "https://admin-banana-test.chunsutech.com/users/roles"
    # Click button:has-text("Create Role")
    page.locator("button:has-text(\"Create Role\")").click()
    # assert page.url == "https://admin-banana-test.chunsutech.com/users/roles/create"
    # Click form div:has-text("Rolename") >> nth=1
    page.locator("form div:has-text(\"Rolename\")").nth(1).click()
    # Click [placeholder="Cannot\ exceed\ 30\ characters"]
    page.locator("[placeholder=\"Cannot\\ exceed\\ 30\\ characters\"]").click()
    # Fill [placeholder="Cannot\ exceed\ 30\ characters"]
    page.locator("[placeholder=\"Cannot\\ exceed\\ 30\\ characters\"]").fill(role_name)
    # Click textarea
    page.locator("textarea").click()
    # Fill textarea
    page.locator("textarea").fill(role_des)
    # Check text=AuthorityALL >> input[type="checkbox"]
    page.locator("text=AuthorityALL >> input[type=\"checkbox\"]").check()
    # Click button:has-text("Confirm")
    # with page.expect_navigation(url="https://admin-banana-test.chunsutech.com/users/roles"):
    with page.expect_navigation():
        page.locator("button:has-text(\"Confirm\")").click()