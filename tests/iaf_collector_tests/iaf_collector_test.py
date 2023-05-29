import os
import time

import pytest
from utils import get_non_empty_result_from_ch
from data_bases.queries import *
from pages.html_first_page import HtmlFirstPage
from constants import *

LOG_FILE = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'network_log.json')


class TestIafCollector:
    class TestHtml1Page:

        @pytest.mark.parametrize('element, event_type, query', [('select', 'caf_form', SELECT_CAF_FORM),
                                                                ('textarea', 'caf_form', SELECT_CAF_FORM),
                                                                ('radio_button', 'caf_form', SELECT_CAF_FORM),
                                                                ('check_box', 'caf_form', SELECT_CAF_FORM),
                                                                ('date_picker', 'caf_form', SELECT_CAF_FORM),
                                                                ('login_input', 'caf_form', SELECT_CAF_FORM),
                                                                ('password_input', 'caf_form', SELECT_CAF_FORM)])
        def test_event_types(self, driver, clickhouse_with_cleaning_raw_events_table, element, event_type, query):
            test_page = HtmlFirstPage(driver, TEST_STAND_URL)
            test_page.get_event_type(element)
            test_page.get_logs_from_network_tab()
            # query_res = get_non_empty_result_from_ch(clickhouse_with_cleaning_raw_events_table, query)
            # assert event_type in query_res[0], f"Event_type '{event_type}' was not found in DB"
            assert test_page.check_event_type_in_logs(LOG_FILE, f'{event_type}')

        def test_slider_event_type(self, driver, clickhouse_with_cleaning_raw_events_table):
            test_page = HtmlFirstPage(driver, TEST_STAND_URL)
            test_page.move_slider()
            test_page.get_logs_from_network_tab()
            # query_res = get_non_empty_result_from_ch(clickhouse_with_cleaning_raw_events_table, SELECT_CAF_FORM)
            # assert 'caf_form' in query_res[0], "Event_type 'caf_form' was not found in DB"
            assert test_page.check_event_type_in_logs(LOG_FILE, 'caf_form')

        def test_page_open_event(self, driver, clickhouse_with_cleaning_raw_events_table):
            test_page = HtmlFirstPage(driver, TEST_STAND_URL)
            driver.refresh()
            test_page.get_logs_from_network_tab()
            # query_res = get_non_empty_result_from_ch(clickhouse_with_cleaning_raw_events_table, SELECT_PAGE_OPEN)
            # assert 'page_open' in query_res[0], "Event_type 'page_open' was not found in DB"
            assert test_page.check_event_type_in_logs(LOG_FILE, 'page_open')

# НУЖНО ИЗМЕНИТЬ РЕАЛИЗАЦИЮ !!!
        @pytest.mark.skip
        def test_page_close_event(self, driver, clickhouse_with_cleaning_raw_events_table):
            test_page = HtmlFirstPage(driver, TEST_STAND_URL)
            test_page.close_tab()
            # test_page.get_logs_from_network_tab()
            query_res = get_non_empty_result_from_ch(clickhouse_with_cleaning_raw_events_table, SELECT_PAGE_CLOSE)
            assert 'page_close' in query_res[0], "Event_type 'page_close' was not found in DB"
            # assert test_page.check_event_type_in_logs(LOG_FILE, 'page_close')

# НУЖНО ИЗМЕНИТЬ РЕАЛИЗАЦИЮ !!!
        @pytest.mark.skip
        def test_page_opened_in_iframe(self, driver, clickhouse_with_cleaning_raw_events_table):
            test_page = HtmlFirstPage(driver, TEST_STAND_URL)
            test_page.get_event_type('iframe_link')
            query_res = get_non_empty_result_from_ch(clickhouse_with_cleaning_raw_events_table, SELECT_IS_IFRAME)
            assert '"is_iframe": true' in query_res[0][0], "Event_type 'page_open' with 'iframe': True parameter was " \
                                                           "not found in DB "

        def test_form_send_event(self, driver, clickhouse_with_cleaning_raw_events_table):
            test_page = HtmlFirstPage(driver, TEST_STAND_URL)
            test_page.press_submit_button()
            test_page.get_logs_from_network_tab()
            # query_res = get_non_empty_result_from_ch(clickhouse_with_cleaning_raw_events_table, SELECT_FORM_SEND)
            # assert 'form_send' in query_res[0], "Event_type 'form_send' was not found in DB"
            assert test_page.check_event_type_in_logs(LOG_FILE, 'form_send')

        def test_scroll_event(self, driver, clickhouse_with_cleaning_raw_events_table):
            test_page = HtmlFirstPage(driver, TEST_STAND_URL)
            test_page.scroll_the_page()
            test_page.get_logs_from_network_tab()
            # query_res = get_non_empty_result_from_ch(clickhouse_with_cleaning_raw_events_table, SELECT_SCROLL)
            # assert 'scroll' in query_res[0], "Event_type 'scroll' was not found in DB"
            assert test_page.check_event_type_in_logs(LOG_FILE, 'scroll')

        def test_pa_enter_event(self, driver, clickhouse_with_cleaning_raw_events_table):
            test_page = HtmlFirstPage(driver, DEV_1_STAND_URL)
            test_page.get_event_type('go_to_pa')
            test_page.get_logs_from_network_tab()
            # query_res = get_non_empty_result_from_ch(clickhouse_with_cleaning_raw_events_table, SELECT_PA_ENTER)
            # assert 'pa_enter' in query_res[0], "Event_type 'pa_enter' was not found in DB"
            assert test_page.check_event_type_in_logs(LOG_FILE, 'pa_enter')
