from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pickle

"""

[ UNDER CONSTRUCTION ]

"""
driver = webdriver.Chrome(service=Service("driver/chromedriver.exe"))

driver.get("https://web.whatsapp.com")

input("Press ENTER after login process.")

with open("whatsapp_cookies.pkl", "wb") as file:
    pickle.dump(driver.get_cookies(), file)

print("Cookies saved.")
driver.quit()
