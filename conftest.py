# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
from datetime import datetime

@pytest.fixture
def driver(request):
    driver = webdriver.Chrome(service=Service("drivers/chromedriver.exe"))
    driver.maximize_window()

    yield driver

    # Get the test report attached to the item
    report = getattr(request.node, "rep_call", None)
    if report and hasattr(report, "outcome") and report.outcome == "failed":
        test_name = request.node.name
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, f"{test_name}_{timestamp}.png")
        driver.save_screenshot(screenshot_path)
        print(f"\n❌ Screenshot saved to: {screenshot_path}")

    driver.quit()

# ✅ Hook: attach the real TestReport to item
def pytest_runtest_makereport(item, call):
    if call.when == "call":
        # call is a TestReport here, safe to store
        item.rep_call = call








