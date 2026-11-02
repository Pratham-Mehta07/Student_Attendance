import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_student_app_loads():
    app_url = os.getenv("STUDENT_APP_URL", "http://localhost:5173")
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")

    with webdriver.Chrome(options=options) as driver:
        driver.get(app_url)
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.TAG_NAME, "body"),
                "Welcome to Student Attendance management app",
            )
        )
