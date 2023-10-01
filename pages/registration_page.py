from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import random
import string

class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.container_home_page = (By.XPATH, "//*[contains(@class, 'columns-container')]")
        self.sign_in_button = (By.XPATH, "//*[contains(@class, 'login')]")
        self.email_field = (By.XPATH, "//*[contains(@class, 'is_required validate account_input form-control')]")
        self.form_notif = (By.XPATH, "//*[contains(@class, 'form-group form-ok')]")
        self.register_button = (By.XPATH, "//*[contains(@class, 'btn btn-default button button-medium exclusive')]")
        self.container_email_registration = (By.XPATH, "//*[contains(@class, 'form-group form-ok')]")
        self.container_detail_info_registration = (By.XPATH, "//*[contains(@class, 'page-subheading')]")
        self.gender1 = (By.XPATH, "//*[contains(@ID, 'uniform-id_gender1')]")
        self.first_name = (By.XPATH, "//*[contains(@ID, 'customer_firstname')]")
        self.second_name = (By.XPATH, "//*[contains(@ID, 'customer_lastname')]")
        self.email_field = (By.XPATH, "//*[contains(@ID, 'email')]")
        self.password_field = (By.XPATH, "//*[contains(@ID, 'passwd')]")
        self.DOB_field = (By.XPATH, "//select[@id='days']/option[@value='2']")
        self.MOB_field = (By.XPATH, "//*[contains(@ID, 'months')]/option[@value='2']")
        self.YOB_field = (By.XPATH, "//*[contains(@ID, 'years')]/option[@value='2004']")
        self.register_button_info = (By.XPATH, "//*[contains(@ID, 'submitAccount')]")
        self.newsletter_checkbox = (By.XPATH, "//*[contains(@ID, 'newsletter')]")
        self.random_string = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))
        self.alert_success_create_account = (By.XPATH, "//*[contains(@class, 'alert alert-success')]")

    def verify_home_page(self):
        try:
            self.driver.find_element(*self.container_home_page)
            return True
        except NoSuchElementException:
            return False

    def click_sign_in_button(self):
        self.driver.find_element(*self.sign_in_button).click()
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(self.container_detail_info_registration, "CREATE AN ACCOUNT"))

    def enter_registration_details(self):
        self.driver.find_element(*self.email_field).send_keys(self.random_string + "@gmail.com")
        time.sleep(5)

    def submit_registration_form(self):
        self.driver.find_element(*self.register_button).click()
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(self.container_detail_info_registration, "YOUR PERSONAL INFORMATION"))

    def input_personal_info_form(self, first_name, last_name, password):
        self.driver.execute_script("window.scrollBy(0, 500);")
        self.driver.find_element(*self.gender1).click()
        self.driver.find_element(*self.first_name).send_keys(first_name)
        self.driver.find_element(*self.second_name).send_keys(last_name)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.DOB_field).click()
        self.driver.find_element(*self.MOB_field).click()
        self.driver.find_element(*self.YOB_field).click()


    def submit_personal_info(self, condition):
        if condition == "with":
            self.driver.find_element(*self.newsletter_checkbox).click()
            self.driver.find_element(*self.register_button_info).click()
        elif condition == "without":
            self.driver.find_element(*self.register_button_info).click()

    def my_account_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(self.alert_success_create_account, "Your account has been created."))
        time.sleep(5)