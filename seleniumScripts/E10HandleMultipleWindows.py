from selenium import webdriver
from selenium.webdriver.common.by import By

driver =webdriver.Chrome(executable_path="C:\DriverChrome\chromedriver")
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/")
parentscreen = driver.current_window_handle
print("parent window is", parentscreen)
driver.find_element(By.XPATH, "//img[@alt='LinkedIn OrangeHRM group']").click()
childwindow=driver.window_handles
print("Type of al windows", type(childwindow))

for child in childwindow:
    print(child)
    if parentscreen!=child:
        print("Switching to screen/tab")
        driver.switch_to.window(child)
        print("Driver tittle is", driver.title)
        #driver.find_element(By.ID, "email-or-phone").send_keys("selenium")
        driver.close()

driver.switch_to.window(parentscreen)
print("Window title", driver.title)
driver.find_element(By.ID, "txtUsername").send_keys("Admin")





