import os
import time

import pytest
from utils import get_non_empty_result_from_ch
from data_bases.queries import *
from iaf_collector_testing_page.html_first_page import HtmlFirstPage
from constants import *


def test_slider_event_type(driver):
    test_page = HtmlFirstPage(driver, 'http://iaf-collector-dev-2.test.env/#page1')
    time.sleep(5)
    r = driver.execute_script('window.localStorage.getItem("Main page");')
    print(r)
