import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CreateNewFacility:
    # @pytest.mark.createnewfacility

    # def test_Create_Facility(self):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  # it is calling driver
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
    # Navigate to Facility Page
    driver.get("https://care.coronasafe.in/facility/create")
    time.sleep(5)
    # Input
    # Wait for the dropdown
    dropdown_menu = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "headlessui-listbox-button-:r1:"))
    )
    dropdown_menu.click()

    # Wait for the options to appear
    options = WebDriverWait(driver, 20).until(
        EC.visibility_of_all_elements_located((By.XPATH, "//ul[@role='listbox']/li[@role='option']"))
    )

    # Click the fourth option
    option_four = options[3]
    option_four.click()
    time.sleep(10)