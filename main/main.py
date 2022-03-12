from pathlib import Path
import sys , os , random , requests , time , pyperclip, multiprocessing, pyautogui
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy , ProxyType
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():

    #Fake useragent
    options = Options()
    ua = UserAgent()
    userAgent = ua.random

    options.add_argument(f'user-agent={userAgent}')

    #Headless mode (set as true to use)
    options.headless = False

    #Don't close the browser
    options.add_experimental_option("detach", True)


    #webdriver

    PATH = "C:\chromedriver.exe"

    driver = webdriver.Chrome(PATH, options=options)
    
    

    #page-action-1

    driver.get('https://app.memrise.com/bienvenue?next=%2Fhome%2F')
   
    dil = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[2]/div[1]/div[1]/button')))
    dil.click()

    seviye = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div[2]/div[3]/div/div[1]/div/button')))
    seviye.click()

    #email

    username_file = open(os.getcwd() + "/usernames.txt", "r" )
    lines = [line.rstrip() for line in username_file]

    chose_random_username_list = random.sample(lines, k=1)

    random_username_string = ''.join(chose_random_username_list)

    random_username_number = str(random.randint(100000, 200000))

    sign = '@gmail.com'

    generated_random_mail = random_username_string + random_username_number + sign

    my_mail = generated_random_mail

    #password

    chose_random_password_list = random.sample(lines, k=1)

    random_password_string = ''.join(chose_random_password_list)

    random_password_number = str(random.randint(10000, 20000))

    generated_random_password = random_password_string + random_password_number

    my_password = generated_random_password

    #page-action-2

    email = WebDriverWait(driver, 20).until(
EC.presence_of_element_located((By.XPATH, '//*[@id="emailAddress"]')))
    email.send_keys(my_mail)

    password = WebDriverWait(driver, 20).until(
EC.presence_of_element_located((By.XPATH, '//*[@id="password"]')))
    password.send_keys(my_password)
          

    kayitbtn = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[3]/div/form/div[3]/button')))
    kayitbtn.click()

    time.sleep(4)

    pyautogui.hotkey('ctrl', 't')

    pyautogui.hotkey('ctrl', '1')

    pyautogui.hotkey('ctrl', 'w')

    time.sleep(1)

    driver.switch_to.window(driver.window_handles[0])

    time.sleep(1)

    driver.get("https://app.memrise.com/aprender/learn?course_id=6165975")

    time.sleep(1)

    nxt = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div[2]/div/div/div/div/div/div[5]/button')))
    nxt.click()


    nxt.click()
    


    answer = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div[2]/div/div/div/div/div/div[4]/div/div[2]/div/div[2]/div[1]/button')))
    answer.click()


    nxt.click()


    xbtn2 = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div[2]/div/div/header/div/div[2]/span[2]/button')))
    xbtn2.click()

    time.sleep(2)

    driver.quit()

    a = 10
    b = 50

    if b > a:
        main()

main()


