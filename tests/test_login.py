from selenium.webdriver.common.by import By
import time

def test_valid_login(driver):
    driver.get("https://www.saucedemo.com/")
    time.sleep(1)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)


    assert "inventory" in driver.current_url




