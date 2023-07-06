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

    # config window locators
    main_page_event_server_url_field = (By.XPATH, "//div[1]/li[2]/input")
    pa_enter_event_server_url_field = (By.XPATH, "//div[2]/li[2]/input")
    main_page_disable_encoding_checkbox = (By.XPATH, "//div[1]/li[12]/input")
    pa_enter__disable_encoding_checkbox = (By.XPATH, "//div[2]/li[8]/input")
    reset_button = (By.XPATH, "//div[3]/div[3]/div[1]")
    save_button = (By.XPATH, "//div[3]/div[3]/div[2]")

    server_event_url = "http://iaf-exchange.test.env/debug_user_event"

    js_script_change_server_event_url = ('''window.localStorage.setItem("Main page", '{"MODE":"eventCollector",'
                                                                                  '"EVENT_SERVER_URL":"https://iaf-exchange.test.env/user_event","IP_DETECTOR_URL":"https://iaf-ip-detector.test.env/","RECAPTCHA_SITE_KEY":"6LfAw4ceAAAAAKq74l-legma9j3XusybaqArZx94","SEND_METRIC_EVENT":"immediately","ALLOWED_USER_EVENTS":"*","SCROLL_DEBOUNCE_TIME":380,"BUFFER_TIME":20000,"GA_ID":"000000000.1111111111","TRACK_UID":"3fa85f64-5717-4562-b3fc-2c963f66afa6","EXTRA_DATA":{},"DISABLE_ENCODING":false}')''')

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

    def change_server_event_url(self):
        self.element_is_visible(self.main_page_event_server_url_field).clear()
        self.element_is_visible(self.main_page_event_server_url_field).send_keys(self.server_event_url)
        self.element_is_visible(self.pa_enter_event_server_url_field).clear()
        self.element_is_visible(self.pa_enter_event_server_url_field).send_keys(self.server_event_url)
        self.element_is_visible(self.save_button).click()

    def switch_to_uncrypted_mode(self):
        self.element_is_visible(self.reset_button).click()
        self.element_is_visible(self.main_page_disable_encoding_checkbox).click()
        self.element_is_visible(self.pa_enter__disable_encoding_checkbox).click()
        self.element_is_visible(self.save_button).click()

    def prepare_test_env(self):
        self.switch_to_uncrypted_mode()
        self.change_server_event_url()
