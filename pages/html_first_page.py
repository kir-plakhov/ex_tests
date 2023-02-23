import random

from locators.html_page_1_locators import HtmlFirstPageLocators
from pages.base_page import BasePage
import time
import json


class HtmlFirstPage(BasePage):
    locators = HtmlFirstPageLocators()

    def get_event_type(self, element):
        elements = {
            "login_input": self.locators.LOGIN_INPUT,
            "password_input": self.locators.PASSWORD_INPUT,
            "select": self.locators.SELECT,
            "radio_button": self.locators.RADIO_BUTTON,
            "check_box": self.locators.CHECK_BOX,
            "slider": self.locators.SLIDER,
            "date_picker": self.locators.DATE_PICKER,
            "page_2_button": self.locators.PAGE_2_BUTTON,
            "iframe_link": self.locators.IFRAME_LINK,
            "textarea": self.locators.TEXT_AREA,
            "submit": self.locators.SUBMIT_BUTTON,
            "go_to_pa": self.locators.GO_TO_PA
        }
        self.element_is_visible(elements[element]).click()

    ''' This method allows to get data from Chrome DevTools Network tab '''
    def get_logs_from_network_tab(self):
        # Sleeps for 10 seconds
        time.sleep(7)
        # Enable Performance Logging of Chrome.

        logs = self.driver.get_log("performance")

        # Opens a writable JSON file and writes the logs in it
        with open("network_log.json", "w", encoding="utf-8") as f:
            f.write("[")

            # Iterates every logs and parses it using JSON
            for log in logs:
                network_log = json.loads(log["message"])["message"]

                # Checks if the current 'method' key has any
                # Network related value.
                if "Network.request" in network_log["method"]:
                    # Writes the network log to a JSON file by
                    # converting the dictionary to a JSON string
                    # using json.dumps().
                    f.write(json.dumps(network_log) + ",")
            f.write("{}]")

    @staticmethod
    def check_event_type_in_logs(file_path, event_type):
        with open(file_path, "rb") as source:
            if rb'\"event_type\":\"%b\"' % event_type.encode("utf-8") in source.read():
                return True
            else:
                return False

    def move_slider(self):
        slider_input = self.element_is_visible(self.locators.SLIDER)
        self.action_drag_and_drop_by_offset(slider_input, random.randint(25, 50), 0)

    def close_tab(self):
        time.sleep(3)
        self.driver.close()

    def press_submit_button(self):
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        time.sleep(1)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    def scroll_the_page(self):
        self.scroll_to_the_bottom()
