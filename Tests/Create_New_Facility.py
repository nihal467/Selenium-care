import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CreateNewFacility:
    # This method is used to create a new facility
    # @pytest.mark.createnewfacility
    # def test_Create_Facility(self):

    # Initialize Chrome driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  # This line initializes the driver
    time.sleep(3)  # This line adds a delay of 3 seconds to the script execution

    # Go to the webpage
    driver.get("https://care.coronasafe.in/")
    time.sleep(5)

    # Enter username "Nihal" in the username field
    username_locator = driver.find_element(By.ID, "username")
    username_locator.send_keys("Nihal")

    # Enter password "Test@123" in the password field
    password_locator = driver.find_element(By.NAME, "password")
    password_locator.send_keys("Test@123")

    # Click the login button
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()
    time.sleep(5)

    # Verify that the URL of the new page contains "https://care.coronasafe.in/facility"
    actual_url = driver.current_url
    assert actual_url == "https://care.coronasafe.in/facility"
    time.sleep(5)

    # Navigate to the Facility Page
    driver.get("https://care.coronasafe.in/facility/create")
    time.sleep(5)

    # Wait for the dropdown - Facility Type
    facility_dropdown_menu = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "headlessui-listbox-button-:r1:"))
    )
    facility_dropdown_menu.click()

    # Wait for the options to appear - Facility Type
    options = WebDriverWait(driver, 20).until(
        EC.visibility_of_all_elements_located((By.XPATH, "//ul[@role='listbox']/li[@role='option']"))
    )

    # Click the fourth option - Facility Type
    option_four = options[3]
    option_four.click()
    time.sleep(4)

    # Fill in the Facility Name
    Facility_Name = driver.find_element(By.NAME, "name")
    Facility_Name.send_keys("Selenium")
    time.sleep(4)

    # Select Features

    # Wait for the dropdown - Feature Type
    # feature_dropdown_menu = WebDriverWait(driver, 20).until(
    #     EC.element_to_be_clickable((By.ID, "headlessui-listbox-button-:r3:"))
    # )
    # feature_dropdown_menu.click()
    #
    # # Wait for the options to appear - Feature Type
    # options = WebDriverWait(driver, 20).until(
    #     EC.visibility_of_all_elements_located((By.XPATH, "//ul[@role='listbox']/li[@role='option']"))
    # )
    #
    # # Click the third and fourth options - Feature Type
    # option_three = options[2]
    # option_three.click()
    # option_four = options[3]
    # option_four.click()
    # time.sleep(4)

    # Fill in the Pincode
    Facility_pincode = driver.find_element(By.NAME, "pincode")
    Facility_pincode.send_keys("682011")
    time.sleep(4)

    # State
    state_dropdown_menu = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "headlessui-listbox-button-:r5:"))
    )
    state_dropdown_menu.click()
    # Wait for the options to appear - State type
    options = WebDriverWait(driver, 20).until(
        EC.visibility_of_all_elements_located((By.XPATH, "//ul[@role='listbox']/li[@role='option']"))
    )
    # Click the first option - State type
    option_one = options[0]
    option_one.click()
    time.sleep(4)

    # District
    district_dropdown_menu = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "headlessui-listbox-button-:r7:"))
    )
    district_dropdown_menu.click()
    # Wait for the options to appear - District type
    options = WebDriverWait(driver, 20).until(
        EC.visibility_of_all_elements_located((By.XPATH, "//ul[@role='listbox']/li[@role='option']"))
    )
    # Click the second option - District type
    option_two = options[1]
    option_two.click()
    time.sleep(4)

    # Local Body
    localbody_dropdown_menu = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "headlessui-listbox-button-:r9:"))
    )
    localbody_dropdown_menu.click()
    # Wait for the options to appear - localbody type
    options = WebDriverWait(driver, 20).until(
        EC.visibility_of_all_elements_located((By.XPATH, "//ul[@role='listbox']/li[@role='option']"))
    )
    # Click the second option - localbody type
    option_two = options[1]
    option_two.click()
    time.sleep(4)

    # Ward
    ward_dropdown_menu = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "headlessui-listbox-button-:rb:"))
    )
    ward_dropdown_menu.click()
    # Wait for the options to appear - ward type
    options = WebDriverWait(driver, 20).until(
        EC.visibility_of_all_elements_located((By.XPATH, "//ul[@role='listbox']/li[@role='option']"))
    )
    # Click the second option - localbody type
    option_two = options[1]
    option_two.click()
    time.sleep(4)

    # Address
    facility_address = driver.find_element(By.NAME, "address")
    facility_address.send_keys("Kasaragod, Kerala, India")
    time.sleep(4)

    # Emergency
    facility_emergency_number = driver.find_element(By.NAME, "phone_number")
    facility_emergency_number.send_keys("9999999999")
    time.sleep(4)

    # Cylinder

    # Location

    #enter submit button
    facility_submit_button = driver.find_element(By.ID, "submit")
    facility_submit_button()
    time.sleep(5)