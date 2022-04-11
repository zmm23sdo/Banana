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
    
def SearchRole(page, admin_rolename):
    # Go to https://admin-banana-test.chunsutech.com/users/roles
    page.goto("https://admin-banana-test.chunsutech.com/users/roles")
    # Fill [placeholder="Select\ the\ property\ search\,\ or\ enter\ a\ keyword\ to\ identify\ the\ search"]
    page.locator("[placeholder=\"Select\\ the\\ property\\ search\\,\\ or\\ enter\\ a\\ keyword\\ to\\ identify\\ the\\ search\"]").fill(admin_rolename)
    # Click .ant-btn.ant-btn-default >> nth=0
    page.locator(".ant-btn.ant-btn-default").first.click()
    page.locator("[aria-label=\"reload\"] svg").click()
    page.locator("text=" + admin_rolename).first.click()

def DeleteRole(page, admin_rolename):
    # Go to https://admin-banana-test.chunsutech.com/users/roles/
    page.goto("https://admin-banana-test.chunsutech.com/users/roles/")
    # Fill [placeholder="Select\ the\ property\ search\,\ or\ enter\ a\ keyword\ to\ identify\ the\ search"]
    page.locator("[placeholder=\"Select\\ the\\ property\\ search\\,\\ or\\ enter\\ a\\ keyword\\ to\\ identify\\ the\\ search\"]").fill(admin_rolename)
    # Click .ant-btn.ant-btn-default >> nth=0
    page.locator(".ant-btn.ant-btn-default").first.click()
    # Click button:has-text("Delete") >> nth=0
    page.locator("button:has-text(\"Delete\")").first.click()
    # Click button:has-text("Confirm")
    page.locator("button:has-text(\"Confirm\")").click()
    # Click .ant-message-notice-content
    page.locator(".ant-message-notice-content").click()
    