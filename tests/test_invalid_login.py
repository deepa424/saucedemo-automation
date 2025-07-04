import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

def test_invalid_login():
    driver = webdriver.Chrome(service=Service("drivers/chromedriver.exe"))
    driver.get("https://www.saucedemo.com/")
    time.sleep(1)

    # Step 1: Enter wrong credentials
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    # Step 2: Assertion and screenshot on failure
    try:
        assert "inventory" in driver.current_url
    except AssertionError:
        # Create folder if it doesn't exist
        os.makedirs("screenshots", exist_ok=True)

        # Generate screenshot path
        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_path = f"screenshots/test_invalid_login_{timestamp}.png"

        # Save screenshot
        driver.save_screenshot(screenshot_path)
        print(f"❌ Screenshot saved to: {os.path.abspath(screenshot_path)}")

        raise  # Re-raise to let pytest mark it as failed
    finally:
        driver.quit()
