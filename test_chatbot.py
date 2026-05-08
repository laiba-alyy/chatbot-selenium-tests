import unittest
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

BASE_URL = os.environ.get("BASE_URL", "http://13.53.217.196:8000")
EMAIL = "laibaali3892@gmail.com"
PASSWORD = "laibs123"

def get_driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    return driver

class ChatbotBuilderTests(unittest.TestCase):

    def test_01_login_page_loads(self):
        driver = get_driver()
        driver.get(f"{BASE_URL}/login")
        self.assertIn("login", driver.current_url.lower())
        driver.quit()

    def test_02_login_has_email_field(self):
        driver = get_driver()
        driver.get(f"{BASE_URL}/login")
        email_field = driver.find_element(By.CSS_SELECTOR, "input[type='email'], input[name='email']")
        self.assertIsNotNone(email_field)
        driver.quit()

    def test_03_login_has_password_field(self):
        driver = get_driver()
        driver.get(f"{BASE_URL}/login")
        password_field = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
        self.assertIsNotNone(password_field)
        driver.quit()

    def test_04_login_has_submit_button(self):
        driver = get_driver()
        driver.get(f"{BASE_URL}/login")
        button = driver.find_element(By.CSS_SELECTOR, "button[type='submit'], button")
        self.assertIsNotNone(button)
        driver.quit()

    def test_05_login_wrong_credentials(self):
        driver = get_driver()
        driver.get(f"{BASE_URL}/login")
        driver.find_element(By.CSS_SELECTOR, "input[type='email'], input[name='email']").send_keys("wrong@email.com")
        driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys("wrongpassword")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit'], button").click()
        time.sleep(2)
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
        email_field = driver.find_element(By.CSS_SELECTOR, "input[type='email'], input[name='email']")
        password_field = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
        self.assertIsNotNone(email_field)
        self.assertIsNotNone(password_field)
        driver.quit()

    def test_08_successful_login(self):
        driver = get_driver()
        driver.get(f"{BASE_URL}/login")
        driver.find_element(By.CSS_SELECTOR, "input[type='email'], input[name='email']").send_keys(EMAIL)
        driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys(PASSWORD)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit'], button").click()
        time.sleep(10)
        self.assertNotIn("login", driver.current_url.lower())
        driver.quit()

    def test_09_dashboard_loads(self):
        driver = get_driver()
        driver.get(f"{BASE_URL}/login")
        driver.find_element(By.CSS_SELECTOR, "input[type='email'], input[name='email']").send_keys(EMAIL)
        driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys(PASSWORD)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit'], button").click()
        time.sleep(10)
        self.assertIn("dashboard", driver.current_url.lower())
        driver.quit()

    def test_10_home_page_loads(self):
        driver = get_driver()
        driver.get(BASE_URL)
        self.assertEqual(driver.current_url.rstrip("/"), BASE_URL)
        driver.quit()

    def test_11_page_title_not_empty(self):
        driver = get_driver()
        driver.get(BASE_URL)
        self.assertNotEqual(driver.title, "")
        driver.quit()

    def test_12_login_then_visit_login_again(self):
        driver = get_driver()
        driver.get(f"{BASE_URL}/login")
        driver.find_element(By.CSS_SELECTOR, "input[type='email'], input[name='email']").send_keys(EMAIL)
        driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys(PASSWORD)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit'], button").click()
        time.sleep(10)
        driver.get(f"{BASE_URL}/login")
        time.sleep(3)
        self.assertNotIn("login", driver.current_url.lower())
        driver.quit()

    def test_13_dashboard_has_content(self):
        driver = get_driver()
        driver.get(f"{BASE_URL}/login")
        driver.find_element(By.CSS_SELECTOR, "input[type='email'], input[name='email']").send_keys(EMAIL)
        driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys(PASSWORD)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit'], button").click()
        time.sleep(3)
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
        driver.get(f"{BASE_URL}/login")
        driver.find_element(By.CSS_SELECTOR, "input[type='email'], input[name='email']").send_keys(EMAIL)
        driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys(PASSWORD)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit'], button").click()
        time.sleep(3)
        self.assertIsNotNone(driver.current_url)
        driver.quit()

if __name__ == "__main__":
    unittest.main()
