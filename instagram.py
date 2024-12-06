from auth_data import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from random import uniform
import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

class Instagram:

    def get_ai_response(self, user_message):

        client = OpenAI(api_key=os.getenv("gpt_token"))

        completion = client.chat.completions.create(

            model="gpt-4-0125-preview",
            messages=[
                {"role": "system", "content": "YOU are ring ai projects assistant and designed to provide never include emojies always information about our service always ill give you message of the use with your previous answers where user: starts for user requests agent: is your responses always give response starting with agent: =, answer in the language of the user"},

                {"role": "user", "content": user_message}
            ]
        )

        ai_response = completion.choices[0].message

        return ai_response.content

    @staticmethod
    def sleep_random():
        sleep(uniform(5, 7))

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.options = webdriver.ChromeOptions()
        # self.options.add_argument('--headless')
        # self.options.add_argument("--window-size=1920,1080")
        self.browser = webdriver.Chrome(options=self.options)
        self.browser.maximize_window()
        self.browser.get("https://www.instagram.com/")



    def check(self, element, by, value):
        try:

            element.find_element(by, value)

            return True

        except NoSuchElementException:

            return False

    def login(self):
        browser = self.browser
        try:
            input_username = browser.find_element(By.NAME, value="username")
            input_username.clear()
            input_username.send_keys(self.username)
            self.sleep_random()
            input_password = browser.find_element(By.NAME, value="password")
            input_password.clear()
            self.sleep_random()
            input_password.send_keys(self.password)
            input_password.send_keys(Keys.ENTER)
            self.sleep_random()
            print("Logined")
            return True
        except:
            return False

    def cancel_notification(self):
        browser = self.browser
        if self.check(browser, By.XPATH, "//div[3]/button[2]"):

            browser.find_element(By.XPATH,
                                     value="//div[3]/button[2]").click()
            print("notification canceled")
            self.sleep_random()
            return True
        print("Not canceled")
        return False
    def open_dm(self):
        browser = self.browser
        if self.check(browser, By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div/div[5]/div/div/div/span/div/a"):
            browser.find_element(By.XPATH,
                                 value="/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div/div[5]/div/div/div/span/div/a").click()

            self.sleep_random()
            print("Dm opened")
            return True
        return False

    def all_new_message_users(self):
        browser = self.browser

        # here im getting all users who sent message new ones
        elements = [chat for chat in browser.find_elements(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div") if self.check(chat, By.XPATH, './div/div/div/div/div[3]/div/div/span')]

        self.sleep_random()

        return elements

    def get_text(self):
        browser = self.browser
        messages = [message.text if message.text.startswith("agent:") else "user: " + message.text for message in browser.find_elements(By.XPATH, "//div/span/div") if message.text]
        self.sleep_random()
        print("Text gotten")
        return messages



    def start(self):
        browser = self.browser
        while not self.login():
            continue

        self.cancel_notification()
        while not self.open_dm():
            self.cancel_notification()
            continue

        self.cancel_notification()




        while True:
            try:
                new_messages = self.all_new_message_users()
                print(new_messages)
                if not new_messages:
                    self.browser.maximize_window()
                    # self.browser.get_screenshot_as_file("screenshot.png")
                    # breakf.cancel_notification()
                    #
                for user in new_messages:
                    user.click()
                    sleep(4)
                    write = browser.find_element(By.XPATH, "//section/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]")
                    write.click()
                    write.send_keys(self.get_ai_response(" , ".join(self.get_text())))
                    sleep(3)
                    write.send_keys(Keys.ENTER)
                    browser.back()
                self.sleep_random()
            except:
                continue

obj = Instagram(username, password)
obj.start()