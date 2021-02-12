from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import datetime

opt=Options()
opt.add_argument("--headless")

driver=webdriver.Chrome(executable_path="C:\DriverChrome\chromedriver",options=opt)
driver.maximize_window()
driver.get("https://www.google.com/")
driver.find_element(By.NAME, "q").send_keys("Huevo")
ts = datetime.datetime.now().timestamp()

time.sleep(3)

driver.quit()


