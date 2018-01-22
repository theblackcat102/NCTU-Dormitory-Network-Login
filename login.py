from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import argparse
chromeOptions = webdriver.ChromeOptions()
# prefs = {"profile.managed_default_content_settings.images": 2}
# chromeOptions.add_experimental_option("prefs", prefs)
chromeOptions.add_argument("--headless")
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--username','-u')
    parser.add_argument('--password','-p')
    args = parser.parse_args()
    return args


def login(username_fill,password_fill):
    driver = webdriver.Chrome('misc/selenium/chromedriver',chrome_options=chromeOptions)

    driver.get("http://140.113.0.38/smsauth/12/pc.php?declare=true&params=pwd&orgi=http://www.nctu.edu.tw/auth/")
    username = driver.find_element_by_name("username")
    password = driver.find_element_by_name("userpwd")
    username.send_keys(username_fill)
    password.send_keys(password_fill)
    driver.find_element_by_name("btlogin").click()

if __name__ == "__main__":
    args = parse_args()
    login(args.username,args.password)


