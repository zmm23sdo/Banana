def CreateCategory(page, admin_categoryname):
    # Go to https://admin-banana-test.chunsutech.com/commodity/category
    page.goto("https://admin-banana-test.chunsutech.com/commodity/category")
    # Click button:has-text("Create")
    page.locator("button:has-text(\"Create\")").click()
    # Click textarea
    page.locator("textarea").click()
    # Fill textarea
    page.locator("textarea").fill(admin_categoryname)
    # Click button:has-text("确 认")
    page.locator("button:has-text(\"确 认\")").click()

def ModifyCategory(page, admin_categoryname, admin_new_categoryname):
    # Go to https://admin-banana-test.chunsutech.com/commodity/category
    page.goto("https://admin-banana-test.chunsutech.com/commodity/category")
    # Click [placeholder="Select\ the\ property\ search\,\ or\ enter\ a\ keyword\ to\ identify\ the\ search"]
    page.locator("[placeholder=\"Select\\ the\\ property\\ search\\,\\ or\\ enter\\ a\\ keyword\\ to\\ identify\\ the\\ search\"]").click()
    # Fill [placeholder="Select\ the\ property\ search\,\ or\ enter\ a\ keyword\ to\ identify\ the\ search"]
    page.locator("[placeholder=\"Select\\ the\\ property\\ search\\,\\ or\\ enter\\ a\\ keyword\\ to\\ identify\\ the\\ search\"]").fill(admin_categoryname)
    # Click .ant-btn.ant-btn-default >> nth=0
    page.locator(".ant-btn.ant-btn-default").first.click()
    # Click [aria-label="reload"] svg
    # page.locator("[aria-label=\"reload\"] svg").click()
    # Click button:has-text("Modify")
    page.locator("button:has-text(\"Modify\")").first.click()
    # Fill textarea:has-text("categoryname")
    page.locator("#name").fill(admin_new_categoryname)
    # Click button:has-text("确 认")
    page.locator("button:has-text(\"确 认\")").click()

def CreateSubcategory(page, admin_categoryname, admin_subcategoryname):
    # Go to https://admin-banana-test.chunsutech.com/commodity/category
    page.goto("https://admin-banana-test.chunsutech.com/commodity/category")
    # Click [placeholder="Select\ the\ property\ search\,\ or\ enter\ a\ keyword\ to\ identify\ the\ search"]
    page.locator("[placeholder=\"Select\\ the\\ property\\ search\\,\\ or\\ enter\\ a\\ keyword\\ to\\ identify\\ the\\ search\"]").click()
    # Fill [placeholder="Select\ the\ property\ search\,\ or\ enter\ a\ keyword\ to\ identify\ the\ search"]
    page.locator("[placeholder=\"Select\\ the\\ property\\ search\\,\\ or\\ enter\\ a\\ keyword\\ to\\ identify\\ the\\ search\"]").fill(admin_categoryname)
    # Click .ant-btn.ant-btn-default >> nth=0
    page.locator(".ant-btn.ant-btn-default").first.click()
    # Click button:has-text("创建子分组")
    page.locator("button:has-text(\"创建子分组\")").click()
    # Click textarea
    page.locator("textarea").click()
    # Fill textarea
    page.locator("textarea").fill(admin_subcategoryname)
    # Click button:has-text("确 认")
    page.locator("button:has-text(\"确 认\")").click()