from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.firefox import GeckoDriverManager

from data_bases.queries import TRUNCATE_RAW_EVENTS
from data_bases.clickHouse_secrets import *
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from clickhouse_driver import Client


@pytest.fixture(scope="function")
def driver():
    desired_capabilities = DesiredCapabilities.CHROME
    desired_capabilities["goog:loggingPrefs"] = {"performance": "ALL"}
    driver = webdriver.Chrome(ChromeDriverManager().install(), desired_capabilities=desired_capabilities)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def clickhouse():
    with Client(
            host=HOST,
            user=USER,
            password=PASSWORD,
    ) as client:
        yield client


@pytest.fixture(scope="function")
def clickhouse_with_cleaning_raw_events_table():
    with Client(
            host=HOST,
            user=USER,
            password=PASSWORD,
    ) as client:
        client.execute(TRUNCATE_RAW_EVENTS)
        yield client
        client.execute(TRUNCATE_RAW_EVENTS)


@pytest.fixture(scope="function")
def driver_firefox():
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.maximize_window()
    yield driver
    driver.quit()



