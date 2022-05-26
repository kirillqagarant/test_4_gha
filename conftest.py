from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def set_headless(headless):
    options = Options()
    options.headless = bool(headless)
    return options


@pytest.fixture
def browser():
#     driver = webdriver.Chrome(ChromeDriverManager().install(), options=set_headless(True))
    driver = webdriver.Remote(command_executor="http://chrome:4444/wd/hub", desired_capabilities=DesiredCapabilities.CHROME)
    driver.set_window_size(1920, 1080)
    driver.get("https://www.google.ru")
    yield driver.title
    driver.quit()
    
