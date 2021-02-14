
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\DriverChrome\chromedriver")
driver.maximize_window()
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")

driver.find_element(By.NAME, "proceed").click()
alt=driver.switch_to.alert

#To capture the alert
alttext= alt.text
print("Text is", alttext )

#To accept the alert
#alt.accept()
time.sleep(3)

#If you want to cancel the alert
alt.dismiss()

driver.find_element(By.NAME, "login").send_keys("Selenium")

driver.quit()



