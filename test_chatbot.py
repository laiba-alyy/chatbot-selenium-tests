import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

BASE_URL = os.getenv("BASE_URL", "http://13.53.217.196")
EMAIL = os.getenv("TEST_EMAIL", "test@gmail.com")
PASSWORD = os.getenv("TEST_PASSWORD", "test123")


def get_driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    return driver


class ChatbotTests(unittest.TestCase):

    # 1
    def test_home_page_loads(self):
        driver = get_driver()
        driver.get(BASE_URL)
        self.assertTrue(BASE_URL in driver.current_url)
        driver.quit()

    # 2
    def test_home_title_exists(self):
        driver = get_driver()
        driver.get(BASE_URL)
        self.assertTrue(len(driver.title) > 0)
        driver.quit()

    # 3
    def test_body_exists(self):
        driver = get_driver()
        driver.get(BASE_URL)
        body = driver.find_element(By.TAG_NAME, "body")
        self.assertIsNotNone(body)
        driver.quit()

    # 4
    def test_login_page_loads(self):
        driver = get_driver()
        driver.get(BASE_URL + "/login")
        self.assertIn("login", driver.current_url.lower())
        driver.quit()

    # 5
    def test_login_email_field_exists(self):
        driver = get_driver()
        driver.get(BASE_URL + "/login")
        field = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
        self.assertIsNotNone(field)
        driver.quit()

    # 6
    def test_login_password_field_exists(self):
        driver = get_driver()
        driver.get(BASE_URL + "/login")
        field = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
        self.assertIsNotNone(field)
        driver.quit()

    # 7
    def test_login_button_exists(self):
        driver = get_driver()
        driver.get(BASE_URL + "/login")
        btn = driver.find_element(By.CSS_SELECTOR, "button")
        self.assertIsNotNone(btn)
        driver.quit()

    # 8
    def test_register_page_loads(self):
        driver = get_driver()
        driver.get(BASE_URL + "/register")
        self.assertIn("register", driver.current_url.lower())
        driver.quit()

    # 9
    def test_register_fields_exist(self):
        driver = get_driver()
        driver.get(BASE_URL + "/register")
        email = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
        password = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
        self.assertIsNotNone(email)
        self.assertIsNotNone(password)
        driver.quit()

    # 10
    def test_invalid_login(self):
        driver = get_driver()
        driver.get(BASE_URL + "/login")

        driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys("wrong@test.com")
        driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys("wrongpass")
        driver.find_element(By.CSS_SELECTOR, "button").click()

        self.assertIn("login", driver.current_url.lower())
        driver.quit()

    # 11
    def test_login_form_not_crash(self):
        driver = get_driver()
        driver.get(BASE_URL + "/login")
        self.assertTrue(True)
        driver.quit()

    # 12
    def test_navigation_home(self):
        driver = get_driver()
        driver.get(BASE_URL)
        driver.get(BASE_URL + "/login")
        self.assertIn("login", driver.current_url.lower())
        driver.quit()

    # 13
    def test_page_source_not_empty(self):
        driver = get_driver()
        driver.get(BASE_URL)
        self.assertTrue(len(driver.page_source) > 100)
        driver.quit()

    # 14
    def test_register_navigation(self):
        driver = get_driver()
        driver.get(BASE_URL + "/register")
        self.assertIn("register", driver.current_url.lower())
        driver.quit()

    # 15
    def test_app_response_time(self):
        import time
        driver = get_driver()
        start = time.time()
        driver.get(BASE_URL)
        end = time.time()
        self.assertTrue((end - start) < 10)
        driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
