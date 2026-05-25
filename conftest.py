import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help="Selecting the website language")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=chrome_options)
    yield browser
    browser.quit()