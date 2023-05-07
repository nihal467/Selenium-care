import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        patient_dob_year_select = driver.find_element(By.XPATH,'//*[@id="year-7"]')
        patient_dob_year_select.click()
        time.sleep(3)
        patient_dob_day=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/main/div/div/div[2]/form/div[1]/div/div/div[4]/div/div/div/div/div/div/div/div[3]/div[25]/div")
        patient_dob_day.click()
        time.sleep(3)
        patient_dob.click()

        gendar_dropdown_menu = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, 'gender-div'))
        )
        gendar_dropdown_menu.click()
        # Wait for the options to appear - gendar type
        options = WebDriverWait(driver, 20).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//ul[@role='listbox']/li[@role='option']"))
        )
        # Click the first option - gendar type
        option_one = options[0]
        option_one.click()
        time.sleep(3)

        current_address=driver.find_element(By.NAME,"address")
        current_address.send_keys("kasaragod, kerala, india")

        pincode_address=driver.find_element(By.ID,"pincode")
        pincode_address.send_keys("682001")
        time.sleep(3)


        local_dropdown_menu = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "local_body"))
        )
        local_dropdown_menu.click()
        # Wait for the options to appear - local type
        options = WebDriverWait(driver, 20).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//ul[@role='listbox']/li[@role='option']"))
        )
        # Click the first option - local type
        option_one = options[0]
        option_one.click()
        time.sleep(3)

        medical_history=driver.find_element(By.NAME,"medical_history_check_1")
        medical_history.click()


        bloodgroup_dropdown_menu = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "blood_group-div"))
        )
        bloodgroup_dropdown_menu.click()
        # Wait for the options to appear - bloodgroup type
        options = WebDriverWait(driver, 20).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//ul[@role='listbox']/li[@role='option']"))
        )
        # Click the first option - Bloodgroup type
        option_one = options[0]
        option_one.click()
        time.sleep(3)

        # Save the patient details

        add_patient_button=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/main/div/div/div[2]/form/div[5]/button[1]")
        add_patient_button.click()
        time.sleep(3)

        # Create a new consultation for the patient as out-patient
        # Consultation Details

        status_during_consultation_dropdown_menu = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "consultation_status"))
        )
        status_during_consultation_dropdown_menu.click()
        # Wait for the options to appear - status during consultation type
        options = WebDriverWait(driver, 20).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//ul[@role='listbox']/li[@role='option']"))
        )
        # Click the 5th option - status during consultation type
        option_one = options[4]
        option_one.click()
        time.sleep(3)


        symptoms_dropdown_menu = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "symptoms"))
        )
        symptoms_dropdown_menu.click()
        # Wait for the options to appear - symptoms
        options = WebDriverWait(driver, 20).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//ul[@role='listbox']/li[@role='option']"))
        )
        # Click the 1st option - Symptoms
        option_one = options[0]
        option_one.click()
        time.sleep(3)

        symptoms_outside=driver.find_element(By.ID,"symptoms")
        symptoms_outside.click()
        time.sleep(3)

        ipnumber=driver.find_element(By.ID,"ip_no")
        ipnumber.send_keys("192.168.1.1")
        time.sleep(3)

        # Diagnosis - since its headless UI dropdown, we should check input field inside iframe

        Provisional = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "icd11_provisional_diagnoses_object"))
        )
        Provisional.click()
        time.sleep(5)
        # Switch to the iframe if it exists
        iframe = driver.find_elements(By.TAG_NAME, 'iframe')
        if iframe:
            driver.switch_to.frame(iframe[0])
        # Find the input field
        input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Select"]'))
        )
        # Enter text into the input field
        input_field.send_keys('1A')
        time.sleep(5)
        # Wait for the options to appear
        options = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, '//ul[@role="listbox"]/li'))
        )
        # Click the first option
        options[2].click()

        diagnosis_outside=driver.find_element(By.ID,"diagnosis")        # a blank click outside to close the droplist
        diagnosis_outside.click()
        time.sleep(3)

        #Treatment Plan

        general_instructions=driver.find_element(By.ID,"consultation_notes")
        general_instructions.send_keys("General advice")
        time.sleep(3)

        verified_by=driver.find_element(By.ID,"verified_by")
        verified_by.send_keys("Dr Selenium")
        time.sleep(3)

        # Create a go to the patient consultation page

        create_consultation_button = driver.find_element(By.ID, "submit")
        create_consultation_button.click()
        time.sleep(5)

        # Verify the redirection URL