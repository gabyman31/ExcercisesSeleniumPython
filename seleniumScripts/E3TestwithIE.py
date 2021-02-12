from selenium import webdriver

driver=webdriver.Ie(executable_path="C:\DriverIE\IEDriverServer")
print(type(driver))
driver.get("https://opensource-demo.orangehrmlive.com/")
myPageTitte=driver.title
print(myPageTitte)
#assert "OrangeHRM" in myPageTitte
driver.quit()

