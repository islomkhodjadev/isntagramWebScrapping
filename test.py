from auth_data import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

instagram = browser.get("https://kun.uz/")
print(instagram)
element = browser.find_element(By.XPATH, "/html/body/div[2]/div/main/div[1]/div[2]/div[2]/div")
elements = element.find_elements(By.XPATH, "/html/body/div[2]/div/main/div[1]/div[2]/div[2]/div/a")

elements[0].find_element(By.CLASS_NAME, "news-lenta__title").click()


# for i in elements:
#     print(i.find_element(By.CLASS_NAME, "news-lenta__title").text)

print(elements)
