import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

BASE_URL = os.getenv("BASE_URL", "http://13.53.217.196")
EMAIL = os.getenv("TEST_EMAIL", "laibaali3892@gmail.com")
PASSWORD = os.getenv("TEST_PASSWORD", "laibs123")


def get_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    return webdriver.Chrome(options=options)


class ChatbotTests(unittest.TestCase):

    def test_01_home_page(self):
        driver = get_driver()
        driver.get(BASE_URL)
        self.assertTrue(driver.title is not None)
        driver.quit()

    def test_02_login_page(self):
        driver = get_driver()
        driver.get(BASE_URL + "/login")
        self.assertIn("login", driver.current_url)
        driver.quit()

    def test_03_register_page(self):
        driver = get_driver()
        driver.get(BASE_URL + "/register")
        self.assertIn("register", driver.current_url)
        driver.quit()

    def test_04_login_email_field(self):
        driver = get_driver()
        driver.get(BASE_URL + "/login")
        email = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
        self.assertIsNotNone(email)
        driver.quit()

    def test_05_login_password_field(self):
        driver = get_driver()
        driver.get(BASE_URL + "/login")
        pwd = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
        self.assertIsNotNone(pwd)
        driver.quit()

    def test_06_login_button(self):
        driver = get_driver()
        driver.get(BASE_URL + "/login")
        btn = driver.find_element(By.CSS_SELECTOR, "button")
        self.assertIsNotNone(btn)
        driver.quit()

    def test_07_invalid_login(self):
        driver = get_driver()
        driver.get(BASE_URL + "/login")
        driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys("wrong@test.com")
        driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys("wrong")
        driver.find_element(By.CSS_SELECTOR, "button").click()
        self.assertIn("login", driver.current_url)
        driver.quit()

    def test_08_page_title(self):
        driver = get_driver()
        driver.get(BASE_URL)
        self.assertTrue(len(driver.title) > 0)
        driver.quit()

    def test_09_body_exists(self):
        driver = get_driver()
        driver.get(BASE_URL)
        body = driver.find_element(By.TAG_NAME, "body")
        self.assertIsNotNone(body)
        driver.quit()

    def test_10_navigation_login(self):
        driver = get_driver()
        driver.get(BASE_URL + "/login")
        self.assertIn("login", driver.current_url)
        driver.quit()


if __name__ == "__main__":
    unittest.main()