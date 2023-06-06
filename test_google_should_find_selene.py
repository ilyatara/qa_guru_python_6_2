import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture(scope="module")
def maximize_browser_window():
    browser.driver.maximize_window()
    # browser.config.window_width = 1920
    # browser.config.window_height = 1080

def test_google_search_positive(maximize_browser_window):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_google_search_negative(maximize_browser_window):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('blablabla').press_enter()
    browser.element('[id="search"]').should(have.no.text('Selene - User-oriented Web UI browser tests in Python'))
