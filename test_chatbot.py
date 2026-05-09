import unittest
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = os.environ.get("BASE_URL", "http://13.53.217.196")
EMAIL = "laibaali3892@gmail.com"
PASSWORD = "laibs123"

def get_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    return driver

def do_login(driver):
    driver.get(f"{BASE_URL}/login")
    time.sleep(2)
    driver.find_element(By.ID, "email").send_keys(EMAIL)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.CSS_SELECTOR, "button.auth-submit-btn").click()
    time.sleep(6)

class ChatbotBuilderTests(unittest.TestCase):

    def test_01_login_page_loads(self):
        driver = get_driver()
        driver.get(f"{BASE_URL}/login")
        self.assertIn("login", driver.current_url.lower())
        driver.quit()

    def test_02_login_has_email_field(self):
        driver = get_driver()
        driver.get(f"{BASE_URL}/login")
        field = driver.find_element(By.ID, "email")
        self.assertIsNotNone(field)
        driver.quit()

    def test_03_login_has_password_field(self):
        driver = get_driver()
        driver.get(f"{BASE_URL}/login")
        field = driver.find_element(By.ID, "password")
        self.assertIsNotNone(field)
        driver.quit()

    def test_04_login_has_submit_button(self):
        driver = get_driver()
        driver.get(f"{BASE_URL}/login")
        button = driver.find_element(By.CSS_SELECTOR, "button.auth-submit-btn")
        self.assertIsNotNone(button)
        driver.quit()

    def test_05_login_wrong_credentials(self):
        driver = get_driver()
        driver.get(f"{BASE_URL}/login")
        time.sleep(2)
        driver.find_element(By.ID, "email").send_keys("wrong@email.com")
        driver.find_element(By.ID, "password").send_keys("wrongpassword")
        driver.find_element(By.CSS_SELECTOR, "button.auth-submit-btn").click()
        time.sleep(4)
        self.assertNotIn("dashboard", driver.current_url.lower())
        driver.quit()

    def test_06_register_page_loads(self):
        driver = get_driver()
        driver.get(f"{BASE_URL}/register")
        self.assertIn("register", driver.current_url.lower())
        driver.quit()

    def test_07_register_has_fields(self):
        driver = get_driver()
        driver.get(f"{BASE_URL}/register")
        email = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
        password = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
        self.assertIsNotNone(email)
        self.assertIsNotNone(password)
        driver.quit()

    def test_08_successful_login(self):
        driver = get_driver()
        do_login(driver)
        self.assertNotIn("login", driver.current_url.lower())
        driver.quit()

    def test_09_dashboard_loads(self):
        driver = get_driver()
        do_login(driver)
        self.assertIn("dashboard", driver.current_url.lower())
        driver.quit()

    def test_10_home_page_loads(self):
        driver = get_driver()
        driver.get(BASE_URL)
        self.assertIsNotNone(driver.current_url)
        driver.quit()

    def test_11_page_title_not_empty(self):
        driver = get_driver()
        driver.get(BASE_URL)
        self.assertNotEqual(driver.title, "")
        driver.quit()

    def test_12_login_then_visit_login_again(self):
        driver = get_driver()
        do_login(driver)
        self.assertIn("dashboard", driver.current_url.lower())
        driver.get(f"{BASE_URL}/login")
        time.sleep(3)
        self.assertNotIn("login", driver.current_url.lower())
        driver.quit()

    def test_13_dashboard_has_content(self):
        driver = get_driver()
        do_login(driver)
        body = driver.find_element(By.TAG_NAME, "body")
        self.assertGreater(len(body.text), 0)
        driver.quit()

    def test_14_app_body_exists(self):
        driver = get_driver()
        driver.get(BASE_URL)
        body = driver.find_element(By.TAG_NAME, "body")
        self.assertIsNotNone(body)
        driver.quit()

    def test_15_login_form_no_crash(self):
        driver = get_driver()
        do_login(driver)
        self.assertIsNotNone(driver.current_url)
        driver.quit()

if __name__ == "__main__":
    unittest.main()
