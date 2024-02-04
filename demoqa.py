from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import configparser
import os

class TestAutomation:

    def __init__(self):
        # Get the directory of the current script
        script_directory = os.path.dirname(os.path.realpath(__file__))

        # Construct the path to the config.ini file
        config_path = os.path.join(script_directory, 'config.ini')

        self.config = configparser.ConfigParser()
        self.config.read(config_path)

        # Specify the path to the ChromeDriver executable
        PATH = "C:\\Program Files (x86)\\chromedriver.exe"

        # Create a Service object with the path to the ChromeDriver executable
        self.chrome_service = Service(PATH)

        # Initialize the WebDriver using the Service object
        self.driver = webdriver.Chrome(service=self.chrome_service)

        self.elements = []

    def navigate_to_website(self):
        website_url = "https://demoqa.com"
        self.driver.get(website_url)

    def store_elements(self):
        self.elements = self.driver.find_elements(By.CLASS_NAME, "card.mt-4.top-card")        

    def test_textbox_input(self, username, email, current_address, permanent_address):
        try:
            self.navigate_to_website()
            self.store_elements()
            if self.elements:
                first_card = self.elements[0]
                first_card.click()
            else:
                print("no element found")

            text_box = self.driver.find_element(By.ID, "item-0")
            text_box.click()  # Prompt the textbox to appear

            username_input = self.driver.find_element(By.ID, "userName")
            email_input = self.driver.find_element(By.ID, "userEmail")
            user_current_address = self.driver.find_element(By.ID, "currentAddress")
            user_permanent_address = self.driver.find_element(By.ID, "permanentAddress")

            username_input.send_keys(username)
            email_input.send_keys(email)
            user_current_address.send_keys(current_address)
            user_permanent_address.send_keys(permanent_address)

            submit_btn = self.driver.find_element(By.ID, "submit")
            self.driver.execute_script("arguments[0].scrollIntoView();", submit_btn) # Scroll submit button into view
            submit_btn.click()

        finally:
            time.sleep(3)
            self.navigate_to_website()

    def test_textbox_input_error(self, username, email, current_address, permanent_address):
        try:
            self.navigate_to_website()
            self.store_elements()

            if self.elements:
                first_card = self.elements[0]
                first_card.click()
            else:
                print("no element found")

            text_box = self.driver.find_element(By.ID, "item-0")
            text_box.click()  # Prompt the textbox to appear

            username_input = self.driver.find_element(By.ID, "userName")
            email_input = self.driver.find_element(By.ID, "userEmail")
            user_current_address = self.driver.find_element(By.ID, "currentAddress")
            user_permanent_address = self.driver.find_element(By.ID, "permanentAddress")

            username_input.send_keys(username)
            email_input.send_keys(email)
            user_current_address.send_keys(current_address)
            user_permanent_address.send_keys(permanent_address)

            submit_btn = self.driver.find_element(By.ID, "submit")
            self.driver.execute_script("arguments[0].scrollIntoView();", submit_btn) # Scroll submit button into view
            submit_btn.click()

        finally:
            time.sleep(3)
            self.navigate_to_website()

    def test_checkbox(self):
        try:
            self.navigate_to_website()
            self.store_elements()

            if self.elements:
                first_card = self.elements[0]
                first_card.click()
            else:
                print("no element found") 

            box = self.driver.find_element(By.ID, "item-1")
            box.click()  # Prompt the checkbox to appear

            checkbox = self.driver.find_element(By.CLASS_NAME, "rct-checkbox")
            checkbox.click()

        finally:
            time.sleep(3)
            self.navigate_to_website()

    def test_radio_button(self):
        try:
            self.navigate_to_website()
            self.store_elements()

            if self.elements:
                first_card = self.elements[0]
                first_card.click()
            else:
                print("no element found") 

            box = self.driver.find_element(By.ID, "item-2")
            box.click()  # Prompt the radiobox to appear

            radiobox = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "yesRadio"))
            )

            # Click on the radio button using JavaScript
            self.driver.execute_script("arguments[0].click();", radiobox)

        finally:
            self.driver.switch_to.default_content()
            time.sleep(3)
            self.navigate_to_website()
    
    def test_web_table_add(self, firstName, lastName, email, age, salary, department):
        try:
            self.navigate_to_website()
            self.store_elements()

            if self.elements:
                first_card = self.elements[0]
                first_card.click()
            else:
                print("no element found") 

            box = self.driver.find_element(By.ID, "item-3")
            box.click()  # Prompt the radiobox to appear

            add_btn = self.driver.find_element(By.ID, "addNewRecordButton")
            add_btn.click()

            firstName_input = self.driver.find_element(By.ID, "firstName")
            lastName_input = self.driver.find_element(By.ID, "lastName")
            email_input = self.driver.find_element(By.ID, "userEmail")
            age_input = self.driver.find_element(By.ID, "age")
            salary_input = self.driver.find_element(By.ID, "salary")
            department_input = self.driver.find_element(By.ID, "department")

            firstName_input.send_keys(firstName)
            lastName_input.send_keys(lastName)
            email_input.send_keys(email)
            age_input.send_keys(age)
            salary_input.send_keys(salary)
            department_input.send_keys(department)

            submit_btn = self.driver.find_element(By.ID, "submit")
            submit_btn.click()
        finally:
            time.sleep(3)
            self.navigate_to_website()

    def test_web_table_search(self, keyword):
        try:
            self.navigate_to_website()
            self.store_elements()

            if self.elements:
                first_card = self.elements[0]
                first_card.click()
            else:
                print("no element found") 

            box = self.driver.find_element(By.ID, "item-3")
            box.click()  # Prompt the radiobox to appear

            search_box = self.driver.find_element(By.ID, "searchBox")
            search_box.click()
            search_box.send_keys(keyword)
            
        finally:
            time.sleep(3)
            self.navigate_to_website()

    def cleanup(self):
        self.driver.quit()

# Usage
if __name__ == "__main__":
    test_automation_instance = TestAutomation()

    try:
        # test_automation_instance.test_textbox_input(
        #     test_automation_instance.config.get('User', 'username'),
        #     test_automation_instance.config.get('User', 'email'),
        #     test_automation_instance.config.get('Address', 'current'),
        #     test_automation_instance.config.get('Address', 'permanent')
        # )

        # test_automation_instance.test_textbox_input_error(
        #     test_automation_instance.config.get('User', 'username'),
        #     test_automation_instance.config.get('User', 'fakeemail'),
        #     test_automation_instance.config.get('Address', 'current'),
        #     test_automation_instance.config.get('Address', 'permanent')
        # )

        # test_automation_instance.test_checkbox()

        # test_automation_instance.test_radio_button()

        # test_automation_instance.test_web_table_add(
        #     test_automation_instance.config.get('WebTable', 'FirstName'),
        #     test_automation_instance.config.get('WebTable', 'LastName'),
        #     test_automation_instance.config.get('WebTable', 'Email'),
        #     test_automation_instance.config.get('WebTable', 'Age'),
        #     test_automation_instance.config.get('WebTable', 'Salary'),
        #     test_automation_instance.config.get('WebTable', 'Department')
        # )

        # test_automation_instance.test_web_table_search(
        #     test_automation_instance.config.get('SearchWord', 'keyword')
        # )

    finally:
        test_automation_instance.cleanup()