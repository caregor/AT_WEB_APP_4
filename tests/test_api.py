"""
Задание 1.
Добавить в проект тесты API, написанные в ходе первого семинара.
"""

import requests
import yaml

from src.api_utils import check_text

with open('config/config.yaml', 'rb') as f:
    data = yaml.safe_load(f)

import requests
import logging

# Настройка логирования
logging.basicConfig(filename='test.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def test_step1(valid_word, invalid_word):
    try:
        assert valid_word in check_text(invalid_word)
    except AssertionError:
        logging.error('test_step1 FAIL')
    except Exception as e:
        logging.exception(f'An unexpected error occurred: {e}')


def test_step2(user_login, post_title):
    try:
        result = requests.get(url=data['api'], headers={'x-auth-token': user_login}, params={'owner': 'notMe'}).json()[
            'data']
        result_title = [i['title'] for i in result]
        assert post_title in result_title
    except AssertionError:
        logging.error('test_step2 FAIL')
    except Exception as e:
        logging.exception(f'An unexpected error occurred: {e}')


# Домашнее Задание №1
def test_step3(user_login, create_post):
    try:
        res = []
        res.append(True) if create_post == 200 else False
        result = requests.get(url=data['api'], headers={'x-auth-token': user_login}, params={'owner': 'Me'}).json()[
            'data']
        result_title = [i['title'] for i in result]
        res.append(True) if data['title'] in result_title else False
        assert all(res)
    except AssertionError:
        logging.error('test_step3 FAIL')
    except Exception as e:
        logging.exception(f'An unexpected error occurred: {e}')
