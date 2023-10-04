import logging

import yaml
from selenium.webdriver.common.by import By

from src.BaseApp import BasePage


class TestSearchLocators:
    ids = dict()
    with open('./locators.yaml', 'rb') as f:
        locators = yaml.safe_load(f)

    for locator in locators['xpath'].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])

    for locator in locators['css'].keys():
        ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])


class OperationsHelper(BasePage):
    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.info(f"Send {word} to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operation with {locator}")
            return False
        return True

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exception with click")
        logging.debug(f"Clicked {element_name} button")
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get text FROM {element_name}")
            return None
        logging.debug(f"We found {text} in field {element_name}")
        return text

    # ENTER TEXT
    def enter_login(self, word):
        logging.debug(TestSearchLocators.ids['LOCATOR_LOGIN_FIELD'])
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_LOGIN_FIELD"], word, description='login')

    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_PASS_FIELD"], word, description='password')

    def enter_name(self, name):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_NAME_FIELD"], name, description='name')

    def enter_email(self, email):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_EMAIL_FIELD"], email, description='email')

    def enter_content(self, content):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTENT_FIELD"], content, description='content')

    # CLICK BTN
    def click_login_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_LOGIN_BTN"], description='login btn')

    def click_contact_link(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_LINK"], description='contact link')

    def click_contact_us_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_US_BTN"], description='contact us button')

    # GET TEXT
    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_ERROR_FIELD"], description='EXCPECTED TEXT')
