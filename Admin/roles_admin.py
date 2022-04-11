def CreateRole(page, admin_rolename, admin_description):
    # Go to https://admin-banana-test.chunsutech.com/dashboard
    page.goto("https://admin-banana-test.chunsutech.com/dashboard")
    # Click .ant-menu-submenu-title .ant-menu-title-content >> nth=0
    page.locator(".ant-menu-submenu-title .ant-menu-title-content").first.click()
    # Click a:has-text("Roles")
    page.locator("a:has-text(\"Roles\")").click()
    # assert page.url == "https://admin-banana-test.chunsutech.com/users/roles"
    # Click button:has-text("Create Role")
    page.locator("button:has-text(\"Create Role\")").click()
    # Fill [placeholder="Cannot\ exceed\ 30\ characters"]
    page.locator("[placeholder=\"Cannot\\ exceed\\ 30\\ characters\"]").fill(admin_rolename)
    # Fill textarea
    page.locator("textarea").fill(admin_description)
    # Check text=AuthorityALL >> input[type="checkbox"]
    page.locator("text=AuthorityALL >> input[type=\"checkbox\"]").check()
    # Click button:has-text("Confirm")
    # with page.expect_navigation(url="https://admin-banana-test.chunsutech.com/users/roles"):
    with page.expect_navigation():
        page.locator("button:has-text(\"Confirm\")").click()
    
   