import time
import os
import requests
import config
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# Assign paths to string variables
current_directory = os.getcwd()
driver_path = os.path.join(current_directory, 'geckodriver.exe') 
binary_path = r'C:\Program Files\Mozilla Firefox\firefox.exe'

# These are necessary to for our Telegram Bot
telegram_bot_token = config.BOT_TOKEN
telegram_chat_id = config.CHAT_ID

# Previous content is kept to be able to catch any change on the page 
previous_content = ''

# Geckodriver Init
options = Options()
options.binary_location = binary_path
service = FirefoxService(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service, options= options)


def check_table(): # Checks a spesific page on the website and compares page with previous version 
    global previous_content
    driver.get("http://hastarandevu.uludag.edu.tr/MiaHbysRandevu")

    modal = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ModalUyariWeb')))

    close_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'Btnuyarikapatweb')))
    close_button.click()

    time.sleep(2)

    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[@onclick="Step01Operation(1)"]')))
    button.click()

    anchor_1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[@onclick="Step02Operation(275)"]')))
    anchor_1.click()

    anchor_2= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[@onclick="Step03Operation(1280)"]')))
    anchor_2.click()


    for i in range(9):
        next_week_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[@onclick="AfterWeek()"]')))
        next_week_button.click()
        time.sleep(1)  

    table_body = driver.find_element(By.ID, 'AjaxTbody')
    current_content = table_body.get_attribute('innerHTML')
    
    if current_content != previous_content and previous_content != '':
        send_notification('Randevu geldi!')
    

    
    previous_content = current_content

def send_notification(message):
    url = f'https://api.telegram.org/bot{telegram_bot_token}/sendMessage'
    payload = {'chat_id': telegram_chat_id, 'text': message}
    response = requests.post(url, json=payload)
    response.raise_for_status()

while True:
    check_table()
    time.sleep(300) # 5 minutes 