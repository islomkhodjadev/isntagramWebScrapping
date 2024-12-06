from auth_data import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
def login(username, password):
    browser = webdriver.Chrome()
    browser.get("https://www.instagram.com/")
    input_username = browser.find_element(By.NAME, value="username")
    input_username.clear()
    input_username.send_keys(username)
    sleep(2)
    input_password = browser.find_element(By.NAME, value="password")
    input_password.clear()
    sleep(2)
    input_password.send_keys(password)
    input_password.send_keys(Keys.ENTER)
    sleep(10)
    try:
        browser.find_element(By.XPATH, value="/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]").click()
        sleep(8)
        browser.find_element(By.XPATH,
                             value="/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div/div[5]/div/div/div/span/div/a").click()

        # chats = browser.find_element(By.XPATH, value="/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[1]/div/div[3]/div/div/div/div/div[2]/div")
        sleep(5)
        browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[1]/div/div[1]/div[2]/div/div").click()
        sleep(3)
        iinput = browser.find_element(By.XPATH, "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/input")
        sleep(2)
        iinput.send_keys("woh.handsome")
        sleep(2)
        browser.find_element(By.XPATH, "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[3]/div/label/div/input").click()
        sleep(5)
        browser.find_element(By.XPATH, "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[4]/div").click()
        sleep(3)

        # iinput.send_keys(Keys.ENTER)
        iinput = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/p")
        iinput.send_keys("Salom")
        sleep(3)
        iinput.send_keys(Keys.ENTER)
    except:
        print("salom")

    # get_cancel = browser.get(r"https://www.instagram.com/direct/inbox/")
    # get_elenent = browser.find_element(By.XPATH, "//button[2]")
    sleep(1000)
    browser.close()
    browser.quit()


login(username, password)
















