import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestCreateNewPatient:
    # This method is used to create a new patient
    #@pytest.mark.createpatient
    #def Create_Patient(self):

        # Initialize Chrome driver
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))  # This line initializes the driver
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

        # Search for Facility

        facility_search= driver.find_element(By.NAME, "search")
        facility_search.click()
        facility_search.send_keys("Selenium")
        time.sleep(3)

        # Go Inside a facility page start with selenium

        facility_view= driver.find_element(By.ID,"facility-details")
        facility_view.click()
        time.sleep(3)

        # Click Manage Patient

        patient_view=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/main/div/div/div[3]/div/div[2]/div[2]/button[3]")
        patient_view.click()
        time.sleep(3)

        # Click Add patient button in the patient tab

        add_patient_details=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/main/div/div/div[2]/div[2]/button[2]")
        add_patient_details.click()
        time.sleep(3)

        # Click the pop-up and select the selenium facility

        # Fill the Patient Form
        # --------------------------------

        patient_phone_number = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/main/div/div/div[2]/form/div[1]/div/div/div[1]/div/div/div/div/input")
        patient_phone_number.send_keys("9999999999")
        time.sleep(10)

        patient_pop_up= driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[3]/div[2]/label")
        patient_pop_up.click()
        time.sleep(3)

        patient_pop_up_submit=driver.find_element(By.ID,"submit")
        patient_pop_up_submit.click()
        time.sleep(3)

        patient_emergency_number = driver.find_element(By.NAME,"emergency_phone_number")
        patient_emergency_number.send_keys("9999999999")
        time.sleep(3)

        patient_name = driver.find_element(By.NAME,"name")
        patient_name.send_keys("Selenium-patient")
        time.sleep(3)

        patient_dob= driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/main/div/div/div[2]/form/div[1]/div/div/div[4]/div/div/div/div/div/div/button/input[2]")
        patient_dob.click()
        time.sleep(3)
        patient_dob_year = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/main/div/div/div[2]/form/div[1]/div/div/div[4]/div/div/div/div/div/div/div/div[1]/div/div/div[2]")
        patient_dob_year.click()
        time.sleep(3)
        patient_dob_backbutton =driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/main/div/div/div[2]/form/div[1]/div/div/div[4]/div/div/div/div/div/div/div/div[1]/div/button[1]")
        patient_dob_backbutton.click()
        time.sleep(3)
        patient_dob_backbutton.click()
        time.sleep(3)
        patient_dob_year_select = driver.find_element(By.XPATH,"//*[@id="year-7"]")
        time.sleep(3)
        patient_dob_month = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/main/div/div/div[2]/form/div[1]/div/div/div[4]/div/div/div/div/div/div/div/div[1]/div/div/div[1]")
        patient_dob_month.click()
        #patient


        # Save the patient details
        # Create a new consultation for the patient
        # Create a go to the patient consultation page
        # Verify the redirection URL

