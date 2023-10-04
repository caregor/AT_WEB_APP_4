import pytest
import requests
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

with open('config/config.yaml', 'rb') as f:
    data = yaml.safe_load(f)
    browser = data['browser']


@pytest.fixture(scope="session")
def browser():
    if browser == 'firefox':
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


s = requests.Session()

@pytest.fixture()
def user_login():
    result = s.post(url=data['url'], data={'username': data['login'], 'password': data['password']})
    response_json = result.json()['token']
    return response_json

@pytest.fixture()
def post_title():
    return 'New Post'

@pytest.fixture()
def valid_word():
    return 'молоко'

@pytest.fixture()
def invalid_word():
    return 'малоко'

@pytest.fixture()
def create_post(user_login):

    result = s.post(url=data['api'], headers={'X-Auth-Token': user_login},
                    data={'title': data['title'], 'description': 'Some desciption', 'content': 'CONTENT'})
    return result.status_code