# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# import pytest
# #
# #
# # chrome_options = webdriver.ChromeOptions()
# # chrome_options.set_capability("browserVersion", "93.0")
# # chrome_options.set_capability("platformName", "Linux")
# # print('set')
# # driver = webdriver.Chrome(
# #     options=chrome_options
# # )
# # print('ok')
# # driver.get("http://localhost:3000")
# # print(driver.title)
# # driver.quit()


# def set_headless(headless):
#     options = Options()
#     options.headless = bool(headless)
#     return options


# @pytest.fixture(scope='function')
# def browser():
#     driver = webdriver.Chrome(ChromeDriverManager().install(), options=set_headless(True))
#     driver.set_window_size(1920, 1080)
#     driver.get("https://www.google.ru")
#     yield driver.title
#     driver.quit()
from requests import get

print(get('http://chrome:5555').status_code)
