from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:\DriverChrome\chromedriver")
print(type(driver))
driver.get("https://opensource-demo.orangehrmlive.com/")
myPageTitte=driver.title
print(myPageTitte)
assert "OrangeHRM" in myPageTitte
driver.quit()


