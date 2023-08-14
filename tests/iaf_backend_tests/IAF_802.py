import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from iaf_collector_testing_page.html_first_page import *
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument(
    "user-agent=Mozilla/5.0(Linux;Android 7.0;SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, Like Gecko) "
    "Chrome/59.0.3071.125 Mobile Safari/537.36")

useragent = "Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Mobile Safari/537.36"

profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", useragent)
options_firefox = webdriver.FirefoxOptions()

page_2_button = (By.XPATH, "/html/body/div[1]/nav/ul/li[2]/button")

url = 'http://iaf-collector.test.env/'
submit_button = (By.XPATH, "/html/body/div[1]/main/div[2]/form/button")
go_to_pa = (By.XPATH, "/html/body/div[1]/main/div[1]/form/button")
check_box = (By.XPATH, "/html/body/div[1]/main/div[4]/form/div[4]/input[1]")


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def driver_firefox():
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options_firefox)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_fake_ua(driver):
    count = 0
    test_page = HtmlFirstPage(driver, url)

    while count < 11:
        driver.refresh()
        count += 1
        time.sleep(1)
    test_page.element_is_visible(go_to_pa).click()
    time.sleep(3)


def test_fake_ua_firefox(driver_firefox):
    count = 0
    test_page = HtmlFirstPage(driver_firefox, url)
    while count < 11:
        test_page.element_is_visible(check_box).click()
        # driver_firefox.refresh()
        count += 1
        time.sleep(1)
    test_page.element_is_visible(go_to_pa).click()
    # time.sleep(30)
