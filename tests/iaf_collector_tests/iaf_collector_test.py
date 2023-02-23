import os
import pytest
from utils import get_non_empty_result_from_ch
from data_bases.queries import *
from pages.html_first_page import HtmlFirstPage
from constants import *


class TestIafCollector:
    class TestHtml1Page:
        LOG_FILE = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'network_log.json')

        @pytest.mark.parametrize('element, event_type, query', [('select', 'caf_form', SELECT_CAF_FORM),
                                                                ('textarea', 'caf_form', SELECT_CAF_FORM),
                                                                ('page_open', 'page_open', SELECT_PAGE_OPEN),
                                                                ('slider', 'caf_form', SELECT_CAF_FORM),
                                                                ('radio_button', 'caf_form', SELECT_CAF_FORM),
                                                                ('check_box', 'caf_form', SELECT_CAF_FORM),
                                                                ('date_picker', 'caf_form', SELECT_CAF_FORM),
                                                                ('login_input', 'caf_form', SELECT_CAF_FORM),
                                                                ('password_input', 'caf_form', SELECT_CAF_FORM)])
        def test_event_types(self, driver, clickhouse_with_cleaning_raw_events_table, element, event_type, query):
            test_page = HtmlFirstPage(driver, TEST_STAND_URL)
            test_page.open()
            if element == 'page_open':
                query_res = get_non_empty_result_from_ch(clickhouse_with_cleaning_raw_events_table, query)
                assert event_type in query_res[0], "Event_type 'page_open' was not found in DB"
                return None
            elif element == 'slider':
                test_page.move_slider()
                query_res = get_non_empty_result_from_ch(clickhouse_with_cleaning_raw_events_table, query)
                assert event_type in query_res[0], "Event_type 'slider' was not found in DB"
                return None
            test_page.get_event_type(element)
            query_res = get_non_empty_result_from_ch(clickhouse_with_cleaning_raw_events_table, query)
            assert event_type in query_res[0], f"Event_type '{event_type}' was not found in DB"

        def test_page_close_event(self, driver, clickhouse_with_cleaning_raw_events_table):
            test_page = HtmlFirstPage(driver, TEST_STAND_URL)
            test_page.open()
            test_page.close_tab()
            query_res = get_non_empty_result_from_ch(clickhouse_with_cleaning_raw_events_table, SELECT_PAGE_CLOSE)
            assert 'page_close' in query_res[0], "Event_type 'page_close' was not found in DB"

        def test_page_opened_in_iframe(self, driver, clickhouse_with_cleaning_raw_events_table):
            test_page = HtmlFirstPage(driver, TEST_STAND_URL)
            test_page.open()
            test_page.get_event_type('iframe_link')
            query_res = get_non_empty_result_from_ch(clickhouse_with_cleaning_raw_events_table, SELECT_IS_IFRAME)
            assert '"is_iframe": true' in query_res[0][0], "Event_type 'page_open' with 'iframe': True parameter was " \
                                                           "not found in DB "

        def test_form_send_event(self, driver, clickhouse_with_cleaning_raw_events_table):
            test_page = HtmlFirstPage(driver, TEST_STAND_URL)
            test_page.open()
            test_page.press_submit_button()
            query_res = get_non_empty_result_from_ch(clickhouse_with_cleaning_raw_events_table, SELECT_FORM_SEND)
            assert 'form_send' in query_res[0], "Event_type 'form_send' was not found in DB"

        def test_scroll_event(self, driver, clickhouse_with_cleaning_raw_events_table):
            test_page = HtmlFirstPage(driver, TEST_STAND_URL)
            test_page.open()
            test_page.scroll_the_page()
            query_res = get_non_empty_result_from_ch(clickhouse_with_cleaning_raw_events_table, SELECT_SCROLL)
            assert 'scroll' in query_res[0], "Event_type 'scroll' was not found in DB"

        def test_pa_enter_event(self, driver, clickhouse_with_cleaning_raw_events_table):
            test_page = HtmlFirstPage(driver, DEV_1_STAND_URL)
            test_page.open()
            test_page.scroll_the_page()
            test_page.get_event_type('go_to_pa')
            query_res = get_non_empty_result_from_ch(clickhouse_with_cleaning_raw_events_table, SELECT_PA_ENTER)
            assert 'pa_enter' in query_res[0], "Event_type 'pa_enter' was not found in DB"


