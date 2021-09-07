from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import pytest


def set_headless(headless):
    options = Options()
    options.headless = bool(headless)
    return options


@pytest.fixture
def browser():
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=set_headless(True))
    driver.set_window_size(1920, 1080)
    driver.get("https://www.google.ru")
    yield driver.title
    driver.quit()
