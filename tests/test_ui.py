"""
    ---Task 1--- HW 3
Добавить в проект тест по проверке механики работы формы Contact Us. Должно проверятся открытие формы, ввод данных в
поля, кликпо кнопке и появление всплывающего alert.
"""
import time

import yaml

from src.testpage import OperationsHelper
import logging

with open('config/config.yaml', 'rb') as f:
    data = yaml.safe_load(f)


def test_step1(browser):
    logging.info("Test UI 1 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login('test')
    testpage.enter_pass('test')
    testpage.click_login_button()
    time.sleep(2)
    assert testpage.get_error_text() == '401'


# Hw Task 1
def test_step2(browser):
    logging.info("Test UI 2 Starting")
    content = ('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et '
               'dolore magna aliqua.')
    logging.info("Test 2 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(data['login'])
    testpage.enter_pass(data['password'])
    testpage.click_login_button()
    testpage.click_contact_link()
    testpage.enter_name('qaa_test')
    testpage.enter_email('qaa@test.test')
    testpage.enter_content(content)
    testpage.click_contact_us_button()
    assert testpage.get_text_dialog_windows() == 'Form successfully submitted'