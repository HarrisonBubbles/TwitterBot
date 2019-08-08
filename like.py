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
        time.sleep(4)
        email = bot.find_element_by_class_name("email-input")
        password = bot.find_element_by_name("session[password]")
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def like_tweet(self, hashtag):
        bot = self.bot
        bot.get("https://twitter.com/search?q=" + hashtag + "&src=typed_query")
        time.sleep(3)
        links = []
        for i in range (1,10):
            bot.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(3)
            tweets = bot.find_elements_by_xpath("//*[@class='css-4rbku5 css-18t94o4 css-901oao r-1re7ezh r-1loqt21 r-1q142lx r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-3s2u2q r-qvutc0']")
            links.extend([elem.get_attribute("href") for elem in tweets])
        links = list(set(links))
        print(len(links))
        for link in links:
            bot.get(link)
            time.sleep(3)
            try:
                fart = bot.find_elements_by_xpath("//*[@class='r-4qtqp9 r-yyyyoo r-50lct3 r-dnmrzs r-bnwqim r-1plcrui r-lrvibr r-1srniue']")
                fart[2].click()
                time.sleep(5)
            except Exception as ex:
                time.sleep(5)

bruh = TwitterBot("enter username here", "enter password here")
bruh.login()
bruh.like_tweet("enter keyword here")
