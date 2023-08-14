import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from iaf_collector_testing_page.html_first_page import HtmlFirstPage

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--headless")

url = 'http://iaf-collector.test.env/'
go_to_pa = (By.XPATH, "/html/body/div[1]/main/div[1]/form/button")
login_input = (By.XPATH, "/html/body/div[1]/main/div[1]/form/div[1]/input")
check_box = (By.XPATH, "/html/body/div[1]/main/div[4]/form/div[4]/input[1]")
user_uid_input = (By.XPATH, "")


@pytest.fixture(scope="function")
def driver_h():
    driver_h = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver_h.maximize_window()
    yield driver_h
    driver_h.quit()


def test_headless(driver_h):
    driver_h.set_window_size(1920, 1080)
    test_page = HtmlFirstPage(driver_h, url)

    user_uid_input = driver_h.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/li[6]/input")
    save_button = driver_h.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[2]")
    user_uid_input.clear()
    print("step clear")
    user_uid_input.send_keys("72bdc79e-4f9d-41dc-a9c0-6d7633102700")
    print("step send_keys")
    save_button.click()
    print("step_click")
    driver_h.refresh()
    print("step_click refresh")
    test_page.element_is_present(go_to_pa).click()
    time.sleep(5)

