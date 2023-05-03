# Open browser
# selenium 4
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestPositiveScenarios:

    @pytest.mark.login
    def test_positive_login(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) # it is calling driver
        time.sleep(3)  # it is delaying the page for a while

        # Go to webpage

        driver.get("https://care.coronasafe.in/")
        time.sleep(5)

        # Type username nihal to usename field

        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("Nihal")

        # Tyoe password to password field

        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("Test@123")

        # Push login button

        submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        submit_button.click()
        time.sleep(5)

        # verify new page url contains & assert use for comparison

        actual_url = driver.current_url
        assert actual_url == "https://care.coronasafe.in/facility"
        time.sleep(5)

        # verify button logout

        logout_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/nav/div[3]/div[4]/div[2]/div[2]/p")
        logout_button.click()
        time.sleep(5)

        # assert logout_button.is_displayed()