from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import InvalidElementStateException
import time
import configparser
import os 

# Get the directory of the current script
script_directory = os.path.dirname(os.path.realpath(__file__))

# Construct the path to the config.ini file
config_path = os.path.join(script_directory, 'config.ini')

config = configparser.ConfigParser()
config.read(config_path)

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://demoqa.com")

elements = driver.find_elements(By.CLASS_NAME, "card.mt-4.top-card")


def test_textbox_input(username, email, current_address, permanent_address):
    if elements:
        first_card = elements[0]
        first_card.click()
    else:
        print("no element found")
    try:
        text_box = driver.find_element(By.ID, "item-0")
        text_box.click()  # Prompt the textbox to appear

        username_input = driver.find_element(By.ID, "userName")
        email_input = driver.find_element(By.ID, "userEmail")
        user_current_address = driver.find_element(By.ID, "currentAddress")
        user_permanent_address = driver.find_element(By.ID, "permanentAddress")

        username_input.send_keys(username)
        email_input.send_keys(email)
        user_current_address.send_keys(current_address)
        user_permanent_address.send_keys(permanent_address)

        submit_btn = driver.find_element(By.ID, "submit")
        driver.execute_script("arguments[0].scrollIntoView();", submit_btn) # Scroll submit button into view
        submit_btn.click()

    finally:
        time.sleep(10)
        driver.close()


def test_textbox_input_error(username, email, current_address, permanent_address):
    if elements:
        first_card = elements[0]
        first_card.click()
    else:
        print("no element found")

    try: 
        text_box = driver.find_element(By.ID, "item-0")
        text_box.click()  # Prompt the textbox to appear

        username_input = driver.find_element(By.ID, "userName")
        email_input = driver.find_element(By.ID, "userEmail")
        user_current_address = driver.find_element(By.ID, "currentAddress")
        user_permanent_address = driver.find_element(By.ID, "permanentAddress")

        username_input.send_keys(username)
        email_input.send_keys(email) # incorrect input
        user_current_address.send_keys(current_address)
        user_permanent_address.send_keys(permanent_address)

        submit_btn = driver.find_element(By.ID, "submit")
        driver.execute_script("arguments[0].scrollIntoView();", submit_btn) # scroll submit button into view
        submit_btn.click()

    finally:
        time.sleep(10)
        driver.close()


# test_textbox_input(
#     config.get('User', 'username'),
#     config.get('User', 'email'),
#     config.get('Address', 'current'),
#     config.get('Address', 'permanent')
# )
        
# test_textbox_input_error(
#     config.get('User', 'username'),
#     config.get('User', 'email'),
#     config.get('Address', 'current'),
#     config.get('Address', 'permanent')
# )