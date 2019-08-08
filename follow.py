from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get("https://twitter.com/")
        time.sleep(3)
        email = bot.find_element_by_class_name("email-input")
        password = bot.find_element_by_name("session[password]")
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def follow(self, hashtag):
        bot = self.bot
        bot.get("https://twitter.com/search?q=" + hashtag + "&src=typed_query")
        time.sleep(3)
        for i in range(1,3):
            bot.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(3)
            tweets = bot.find_elements_by_xpath("//*[@class='css-4rbku5 css-18t94o4 css-1dbjc4n r-sdzlij r-1loqt21 r-1adg3ll r-1udh08x r-13qz1uu']")
            links = [elem.get_attribute("href") 
                    for elem in tweets]
            print(len(links))
            for link in links:
                bot.get(link)
                time.sleep(3)
                try:
                    fart = bot.find_elements_by_xpath("//*[@class='css-18t94o4 css-1dbjc4n r-1niwhzg r-p1n3y5 r-sdzlij r-1phboty r-rs99b7 r-1w2pmg r-1vuscfd r-1dhvaqw r-1fneopy r-o7ynqc r-6416eg r-lrvibr']")
                    fart[0].click()
                    time.sleep(10)
                except Exception as ex:
                    time.sleep(5)

bruh = TwitterBot("enter username here", "enter password here")
bruh.login()
bruh.follow("enter hashtag here")
