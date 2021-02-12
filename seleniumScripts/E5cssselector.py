from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(executable_path="C:\DriverChrome\chromedriver")
print(type(driver))
driver.get("https://opensource-demo.orangehrmlive.com/")
myPageTitte=driver.title
print(myPageTitte)

driver.find_element(By.XPATH, "//*[@id='txtUsername']").send_keys("Admin")
driver.find_element(By.CSS_SELECTOR,"input[type='password']").send_keys("admin123")
driver.find_element(By.XPATH, "//*[@id='btnLogin']").click()
print("The URL after login is ", driver.current_url)
assert "dashboard" in driver.current_url
driver.find_element(By.XPATH, "//*[@id='welcome']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//*[@id='welcome-menu']/ul/li[2]/a").click()
assert "login" in driver.current_url

# Test Fogot Password
driver.find_element(By.LINK_TEXT, "Forgot your password?").click()
driver.find_element(By.TAG_NAME, "img").click()

driver.quit()