import pytest
import requests
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    name = testdata['user']
    passwd = testdata['pass']


@pytest.fixture(scope="session")
def browser():
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture()
def login():
    r = requests.post('https://test-stand.gb.ru/gateway/login', data={'username': name, 'password': passwd})
    return r.json()['token']


@pytest.fixture()
def font_size():
    return "32px"


@pytest.fixture()
def text_answer():
    return '0 error(s)'
