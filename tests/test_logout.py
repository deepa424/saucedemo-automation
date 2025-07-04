from selenium.webdriver.common.by import By
import time

def test_logout(driver):
    driver.get("https://www.saucedemo.com/")
    time.sleep(1)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    driver.find_element(By.ID, "react-burger-menu-btn").click()
    time.sleep(2)
    driver.find_element(By.ID, "logout_sidebar_link").click()
    time.sleep(2)

    assert "saucedemo.com" in driver.current_url
