import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class CreateNewPatient:
    # This method is used to create a new facility
    # @pytest.mark.createpatient
    #def test_Create_Patient(self):

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
    # Save the patient details
    # Create a new consultation for the patient
    # Create a go to the patient consultation page
    # Verify the redirection URL
