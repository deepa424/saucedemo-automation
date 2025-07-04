import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_to_cart(driver):
    driver.get("https://www.saucedemo.com/")

    # Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Wait for inventory to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
    )

    # Add item to cart
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    # Click on cart icon
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Wait for cart page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "checkout"))
    )

    # Click checkout
    driver.find_element(By.ID, "checkout").click()

    # Wait for next step and assert
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "continue"))
    )

    assert "checkout-step-one" in driver.current_url




