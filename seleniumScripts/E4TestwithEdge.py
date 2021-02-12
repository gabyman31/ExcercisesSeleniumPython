from selenium import webdriver

driver=webdriver.Edge(executable_path="C:\EdgeDriver\msedgedriver")
print(type(driver))
driver.get("https://opensource-demo.orangehrmlive.com/")
myPageTitte=driver.title
print(myPageTitte)
assert "OrangeHRM" in myPageTitte
driver.quit()
