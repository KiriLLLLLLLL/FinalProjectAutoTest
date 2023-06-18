import logging
import time
import yaml
from testpage import OperationsHelper

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_step1(browser, font_size):
    logging.info("Test1 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata["user"])
    testpage.enter_pass(testdata["pass"])
    testpage.click_login_button()
    testpage.click_about_button()
    time.sleep(3)

    assert testpage.get_about_page_font() == font_size


def test_step2(browser, text_answer):
    logging.info("Test2 Starting")
    testpage = OperationsHelper(browser)

    assert testpage.get_answer_from_nikto(testdata['nikto'], text_answer)


def test_step3(browser, login):
    logging.info("Test3 Starting")
    testpage = OperationsHelper(browser)

    assert testpage.get_user_profile(login) == testdata["user"]


