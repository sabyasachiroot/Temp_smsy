import requests
from termcolor import colored
from colorama import init
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import phonenumbers
from phonenumbers import geocoder

# Developed By Cmmd_kalishnikova

init()
num_html = requests.get('https://receive-smss.com/inactive-numbers/')
if len(num_html.text) >= 10000:
    print(colored('WEBSITE ACTIVE !', 'green'))
else:
    print(colored('WEBSITE INACTIVE !!!!!!!!!' , 'red'))

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

try:
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://receive-smss.com/login/')
    user = driver.find_element(By.NAME , 'log')
    pwd = driver.find_element(By.NAME , 'pwd')
    submit = driver.find_element(By.NAME , 'wp-submit')
    user.send_keys('venom@2024')
    pwd.send_keys('2005')
    submit.click()
    driver.implicitly_wait(5)
    print(colored('LOGIN SUCCESSFULLY' , 'green'))

    number = driver.find_elements(By.CLASS_NAME , 'number-boxes-itemm-number')
    for nums in number:
        phn = phonenumbers.parse(nums.text)
        ctry = geocoder.description_for_number(phn , 'en')
        print(f'{ctry} ==> {nums.text}')
except Exception:
    print(Exception)








