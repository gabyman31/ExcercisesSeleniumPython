from selenium import webdriver

driver=webdriver.Firefox(executable_path="C:\DriverFirefox\geckodriver")
print(type(driver))
driver.get("https://opensource-demo.orangehrmlive.com/")
myPageTitte=driver.title
print(myPageTitte)
assert "OrangeHRM" in myPageTitte
driver.quit()