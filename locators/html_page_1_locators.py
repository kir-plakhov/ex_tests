from selenium.webdriver.common.by import By


class HtmlFirstPageLocators:
    PAGE_1_BUTTON = (By.CSS_SELECTOR, "button[class='button page1']")
    PAGE_2_BUTTON = (By.CSS_SELECTOR, "button[class='button page2']")
    LOGIN_INPUT = (By.CSS_SELECTOR, "input[id='login']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[id='password']")
    RADIO_BUTTON = (By.CSS_SELECTOR, "input[id='radio1']")
    CHECK_BOX = (By.CSS_SELECTOR, "input[id='check1']")
    DATE_PICKER = (By.CSS_SELECTOR, "input[id='datepicker']")
    SLIDER = (By.CSS_SELECTOR, "input[id='range']")
    TEXT_AREA = (By.CSS_SELECTOR, "textarea[id='textarea']")
    SUBMIT_BUTTON = (By.XPATH, "/html/body/div[1]/main/div[2]/form/button")
    SELECT = (By.CSS_SELECTOR, "select[id='select']")
    IFRAME_LINK = (By.CSS_SELECTOR, "a[href='/iframe.html']")
    GO_TO_PA = (By.XPATH, '/html/body/div[1]/main/div[1]/form/button')

