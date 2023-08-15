import os
import time
import pytest
from utils import get_non_empty_result_from_ch, get_logs_from_network_tab
from data_bases.queries import *
from iaf_collector_testing_page.html_first_page import HtmlFirstPage
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
        def test_event_types(self, driver, element, event_type, query):
            test_page = HtmlFirstPage(driver, DEV_2_STAND_URL)
            test_page.switch_to_uncrypted_mode()
            test_page.get_event_type(element)
            get_logs_from_network_tab(driver)
            assert test_page.check_event_type_in_logs(LOG_FILE, f'{event_type}'), f'{event_type} has not been found in LOG_FILE'

        def test_slider_event_type(self, driver):
            test_page = HtmlFirstPage(driver, DEV_2_STAND_URL)
            test_page.switch_to_uncrypted_mode()
            test_page.move_slider()
            get_logs_from_network_tab(driver)
            assert test_page.check_event_type_in_logs(LOG_FILE, 'caf_form'), 'caf_form event_type has not been found in LOG_FILE'

        def test_page_open_event(self, driver):
            test_page = HtmlFirstPage(driver, DEV_2_STAND_URL)
            test_page.switch_to_uncrypted_mode()
            driver.refresh()
            get_logs_from_network_tab(driver)
            assert test_page.check_event_type_in_logs(LOG_FILE, 'page_open'), 'page_open event_type has not been found in LOG_FILE'

# НУЖНО ИЗМЕНИТЬ РЕАЛИЗАЦИЮ !!!
        @pytest.mark.skip
        def test_page_close_event(self, driver, clickhouse_with_cleaning_raw_events_table):
            test_page = HtmlFirstPage(driver, DEV_2_STAND_URL)
            test_page.switch_to_uncrypted_mode()
            test_page.change_server_event_url()
            test_page.close_tab()
            query_res = get_non_empty_result_from_ch(clickhouse_with_cleaning_raw_events_table, SELECT_PAGE_CLOSE)
            assert 'page_close' in query_res[0], "Event_type 'page_close' was not found in DB"

        # НУЖНО ИЗМЕНИТЬ РЕАЛИЗАЦИЮ !!!
        @pytest.mark.skip
        def test_page_opened_in_iframe(self, driver, clickhouse_with_cleaning_raw_events_table):
            test_page = HtmlFirstPage(driver, DEV_2_STAND_URL)
            test_page.switch_to_uncrypted_mode()
            test_page.change_server_event_url()
            test_page.get_event_type('iframe_link')
            query_res = get_non_empty_result_from_ch(clickhouse_with_cleaning_raw_events_table, SELECT_IS_IFRAME)
            assert '"is_iframe": true' in query_res[0][0], "Event_type 'page_open' with 'iframe': True parameter was " \
                                                           "not found in DB "

        def test_form_send_event(self, driver):
            test_page = HtmlFirstPage(driver, DEV_2_STAND_URL)
            test_page.switch_to_uncrypted_mode()
            test_page.press_submit_button()
            get_logs_from_network_tab(driver)
            assert test_page.check_event_type_in_logs(LOG_FILE, 'form_send'), 'form_send event_type has not been found in LOG_FILE'

        def test_scroll_event(self, driver):
            test_page = HtmlFirstPage(driver, DEV_2_STAND_URL)
            test_page.switch_to_uncrypted_mode()
            test_page.scroll_the_page()
            get_logs_from_network_tab(driver)
            assert test_page.check_event_type_in_logs(LOG_FILE, 'scroll'), 'scroll event_type has not been found in LOG_FILE'

        def test_pa_enter_event(self, driver):
            test_page = HtmlFirstPage(driver, DEV_2_STAND_URL)
            test_page.switch_to_uncrypted_mode()
            test_page.get_event_type('go_to_pa')
            get_logs_from_network_tab(driver)
            assert test_page.check_event_type_in_logs(LOG_FILE, 'pa_enter'), 'pa_enter event_type has not been found in LOG_FILE'

