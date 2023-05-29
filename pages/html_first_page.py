import random
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time
import json


class HtmlFirstPage(BasePage):

    # Locators
    page_1_button = (By.XPATH, "/html/body/div[1]/nav/ul/li[1]/button")
    page_2_button = (By.XPATH, "/html/body/div[1]/nav/ul/li[2]/button")
    login_input = (By.XPATH, "/html/body/div[1]/main/div[1]/form/div[1]/input")
    password_input = (By.XPATH, "/html/body/div[1]/main/div[1]/form/div[2]/input")
    radio_button = (By.XPATH, "/html/body/div[1]/main/div[4]/form/div[3]/input[1]")
    check_box = (By.XPATH, "/html/body/div[1]/main/div[4]/form/div[4]/input[1]")
    date_picker = (By.XPATH, "/html/body/div[1]/main/div[4]/form/div[6]/input")
    slider = (By.XPATH, "/html/body/div[1]/main/div[4]/form/div[5]/input")
    text_area = (By.XPATH, "/html/body/div[1]/main/div[4]/form/div[2]/textarea")
    submit_button = (By.XPATH, "/html/body/div[1]/main/div[2]/form/button")
    select = (By.XPATH, "/html/body/div[1]/main/div[4]/form/div[1]/select")
    iframe_link = (By.XPATH, "/html/body/footer/a")
    go_to_pa = (By.XPATH, "/html/body/div[1]/main/div[1]/form/button")
    go_to_google_page = (By.XPATH, "/html/body/div[1]/main/div[1]/ul/li[5]/a")
    ga_id_input = (By.XPATH, "/html/body/div/div[2]/div[1]/li[9]/input")




    def get_event_type(self, element):
        elements = {
            "login_input": self.login_input,
            "password_input": self.password_input,
            "select": self.select,
            "radio_button": self.radio_button,
            "check_box": self.check_box,
            "slider": self.slider,
            "date_picker": self.date_picker,
            "page_2_button": self.page_2_button,
            "iframe_link": self.iframe_link,
            "textarea": self.text_area,
            "submit": self.submit_button,
            "go_to_pa": self.go_to_pa
        }
        self.element_is_visible(elements[element]).click()

    ''' This method allows to get data from Chrome DevTools Network tab '''
    def get_logs_from_network_tab(self):
        # Sleeps for 10 seconds
        time.sleep(10)
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
        slider_input = self.element_is_visible(self.slider)
        self.action_drag_and_drop_by_offset(slider_input, random.randint(25, 50), 0)

    def close_tab(self):
        time.sleep(3)
        self.driver.close()

    def press_submit_button(self):
        self.element_is_visible(self.submit_button).click()
        time.sleep(1)
        self.element_is_visible(self.submit_button).click()

    def scroll_the_page(self):
        self.scroll_to_the_bottom()

    def add_tab(self):
        self.element_is_visible(self.page_2_button).click()
        self.element_is_visible(self.go_to_google_page).click()
        self.driver.switch_to.window(self.driver.window_handles[0])
