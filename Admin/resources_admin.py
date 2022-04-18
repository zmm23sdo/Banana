def AddGroup(page, admin_groupname):
    # Go to https://admin-banana-dev.chunsutech.com/resources/
    page.goto("https://admin-banana-dev.chunsutech.com/resources/")
    # Click button:has-text("Add") >> nth=0
    page.locator("button:has-text(\"Add\")").first.click()
    # Fill [placeholder="请输入"]
    page.locator("[placeholder=\"请输入\"]").fill(admin_groupname)
    # Click button:has-text("确 认")
    page.locator("button:has-text(\"确 认\")").click()

def AddSubgroup(page, admin_groupname, admin_subgroupname):
    # Go to https://admin-banana-dev.chunsutech.com/resources/
    page.goto("https://admin-banana-dev.chunsutech.com/resources/")
    # Click text=Group1650252144
    page.locator("text="+admin_groupname).click()
    # Click button:has-text("Add") >> nth=0
    page.locator("button:has-text(\"Add\")").first.click()
    # Fill [placeholder="请输入"]
    page.locator("[placeholder=\"请输入\"]").fill(admin_subgroupname)
    # Click button:has-text("确 认")
    page.locator("button:has-text(\"确 认\")").click()

def ChangeGroup(page, admin_groupname, admin_new_groupname):
    # Go to https://admin-banana-dev.chunsutech.com/resources/
    page.goto("https://admin-banana-dev.chunsutech.com/resources/")
    # Click [placeholder="Search\ Group\ Name"]
    page.locator("[placeholder=\"Search\\ Group\\ Name\"]").click()
    # Fill [placeholder="Search\ Group\ Name"]
    page.locator("[placeholder=\"Search\\ Group\\ Name\"]").fill(admin_groupname)
    # Click text=Undefined GroupingnameGroup1650252144Group1650260630cAddChangeDelete >> button >> nth=0
    page.locator("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div > div.ant-row.row___1tEsv > div.ant-col.ant-col-6.col___3c_cy > div.searchContainer___16Y5a > span > span > span > button").first.click()
    # Click text=Group1650252144
    page.locator("text="+admin_groupname).click()
    # Click button:has-text("Change")
    page.locator("button:has-text(\"Change\")").click()
    # Fill [placeholder="请输入"]
    page.locator("[placeholder=\"请输入\"]").fill(admin_new_groupname)
    # Click button:has-text("确 认")
    page.locator("button:has-text(\"确 认\")").click()

def ChangeSubgroup(page, admin_subgroupname, admin_new_subgroupname):
    # Go to https://admin-banana-dev.chunsutech.com/resources/
    page.goto("https://admin-banana-dev.chunsutech.com/resources/")
    # Click [placeholder="Search\ Group\ Name"]
    page.locator("[placeholder=\"Search\\ Group\\ Name\"]").click()
    # Fill [placeholder="Search\ Group\ Name"]
    page.locator("[placeholder=\"Search\\ Group\\ Name\"]").fill(admin_subgroupname)
    # Click text=Undefined GroupingnameGroup1650252144Group1650260630cAddChangeDelete >> button >> nth=0
    page.locator("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div > div.ant-row.row___1tEsv > div.ant-col.ant-col-6.col___3c_cy > div.searchContainer___16Y5a > span > span > span > button").first.click()
    # Click .ant-tree-switcher.ant-tree-switcher_close
    page.locator("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div > div.ant-row.row___1tEsv > div.ant-col.ant-col-6.col___3c_cy > div.ant-tree.ant-tree-icon-hide.tree___3L19m > div.ant-tree-list > div > div > div > div.ant-tree-treenode.ant-tree-treenode-switcher-close.ant-tree-treenode-leaf-last > span.ant-tree-switcher.ant-tree-switcher_close > span > svg").click()
    # Click text=Sub_Group1650260630
    page.locator("text="+admin_subgroupname).click()
    # Click button:has-text("Change")
    page.locator("button:has-text(\"Change\")").click()
    # Click [placeholder="请输入"]
    page.locator("[placeholder=\"请输入\"]").click()
    # Fill [placeholder="请输入"]
    page.locator("[placeholder=\"请输入\"]").fill(admin_new_subgroupname)
    # Click button:has-text("确 认")
    page.locator("button:has-text(\"确 认\")").click()

def DeleteSubgroup(page, admin_subgroupname):
    # Go to https://admin-banana-dev.chunsutech.com/resources/
    page.goto("https://admin-banana-dev.chunsutech.com/resources/")
    # Click [placeholder="Search\ Group\ Name"]
    page.locator("[placeholder=\"Search\\ Group\\ Name\"]").click()
    # Fill [placeholder="Search\ Group\ Name"]
    page.locator("[placeholder=\"Search\\ Group\\ Name\"]").fill(admin_subgroupname)
    # Click text=Undefined GroupingnameGroup1650252144Group1650260630cAddChangeDelete >> button >> nth=0
    page.locator("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div > div.ant-row.row___1tEsv > div.ant-col.ant-col-6.col___3c_cy > div.searchContainer___16Y5a > span > span > span > button").first.click()
    # Click .ant-tree-switcher.ant-tree-switcher_close
    page.locator("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div > div.ant-row.row___1tEsv > div.ant-col.ant-col-6.col___3c_cy > div.ant-tree.ant-tree-icon-hide.tree___3L19m > div.ant-tree-list > div > div > div > div.ant-tree-treenode.ant-tree-treenode-switcher-close.ant-tree-treenode-leaf-last > span.ant-tree-switcher.ant-tree-switcher_close > span > svg").click()
    # Click text=Sub_Group1650260630
    page.locator("text="+admin_subgroupname).click()
    # Click button:has-text("Delete") >> nth=0
    page.locator("button:has-text(\"Delete\")").first.click()
    # Click button:has-text("Confirm")
    page.locator("button:has-text(\"Confirm\")").click()

def DeleteGroup(page, admin_groupname):
    # Go to https://admin-banana-dev.chunsutech.com/resources/
    page.goto("https://admin-banana-dev.chunsutech.com/resources/")
    # Click [placeholder="Search\ Group\ Name"]
    page.locator("[placeholder=\"Search\\ Group\\ Name\"]").click()
    # Fill [placeholder="Search\ Group\ Name"]
    page.locator("[placeholder=\"Search\\ Group\\ Name\"]").fill(admin_groupname)
    # Click text=Undefined GroupingnameGroup1650252144Group1650260630cAddChangeDelete >> button >> nth=0
    page.locator("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div > div.ant-row.row___1tEsv > div.ant-col.ant-col-6.col___3c_cy > div.searchContainer___16Y5a > span > span > span > button").first.click()
    # Click text=Group1650252144
    page.locator("text="+admin_groupname).click()
    # Click button:has-text("Delete") >> nth=0
    page.locator("button:has-text(\"Delete\")").first.click()
    # Click button:has-text("Confirm")
    page.locator("button:has-text(\"Confirm\")").click()

def AddImage(page, admin_groupname):
    # Go to https://admin-banana-dev.chunsutech.com/resources/
    page.goto("https://admin-banana-dev.chunsutech.com/resources/")
    # Click [placeholder="Search\ Group\ Name"]
    page.locator("[placeholder=\"Search\\ Group\\ Name\"]").click()
    # Fill [placeholder="Search\ Group\ Name"]
    page.locator("[placeholder=\"Search\\ Group\\ Name\"]").fill(admin_groupname)
    # Click text=Undefined GroupingnameGroup1650252144Group1650260630cAddChangeDelete >> button >> nth=0
    page.locator("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div > div.ant-row.row___1tEsv > div.ant-col.ant-col-6.col___3c_cy > div.searchContainer___16Y5a > span > span > span > button").first.click()
    # Click text=Group1650252144
    page.locator("text="+admin_groupname).click()
    # Upload 0001.jpg
    page.set_input_files('input[type="file"]',"/Users/michaelcheung/Project/Banana/Pictures/0001.jpg")
    # Click text=Add ImageImage Name >> button >> nth=1
    page.locator("text=Add ImageImage Name >> button").nth(1).click()

def ChangeImageGroup(page, admin_groupname):
    # Go to https://admin-banana-dev.chunsutech.com/resources/
    page.goto("https://admin-banana-dev.chunsutech.com/resources/")
    # Click [placeholder="Search\ Group\ Name"]
    page.locator("[placeholder=\"Search\\ Group\\ Name\"]").click()
    # Fill [placeholder="Search\ Group\ Name"]
    page.locator("[placeholder=\"Search\\ Group\\ Name\"]").fill(admin_groupname)
    # Click text=Undefined GroupingnameGroup1650252144Group1650260630cAddChangeDelete >> button >> nth=0
    page.locator("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div > div.ant-row.row___1tEsv > div.ant-col.ant-col-6.col___3c_cy > div.searchContainer___16Y5a > span > span > span > button").first.click()
    # Click text=Group1650252144
    page.locator("text="+admin_groupname).click()
    # Click td >> nth=0
    page.locator("td").first.click()
    # Click button:has-text("修改分组")
    page.locator("button:has-text(\"修改分组\")").click()
    # Click #first_id
    page.locator("#first_id").click()
    # Click .ant-select-item >> nth=0
    page.locator(".ant-select-item").first.click()
    # Click button:has-text("确 认")
    page.locator("button:has-text(\"确 认\")").click()

def DeleteImage(page, admin_groupname):
    # Go to https://admin-banana-dev.chunsutech.com/resources/
    page.goto("https://admin-banana-dev.chunsutech.com/resources/")
    # Click [placeholder="Search\ Group\ Name"]
    page.locator("[placeholder=\"Search\\ Group\\ Name\"]").click()
    # Fill [placeholder="Search\ Group\ Name"]
    page.locator("[placeholder=\"Search\\ Group\\ Name\"]").fill(admin_groupname)
    # Click text=Undefined GroupingnameGroup1650252144Group1650260630cAddChangeDelete >> button >> nth=0
    page.locator("#root > div > section > div.ant-layout > main > div > div.ant-pro-grid-content > div > div > div > div.ant-row.row___1tEsv > div.ant-col.ant-col-6.col___3c_cy > div.searchContainer___16Y5a > span > span > span > button").first.click()
    # Click text=Group1650252144
    page.locator("text="+admin_groupname).click()
    # Click td >> nth=0
    page.locator("td").first.click()
    # Click button:has-text("Delete") >> nth=1
    page.locator("button:has-text(\"Delete\")").nth(1).click()