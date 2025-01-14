# Pytest configuration file
# See https://docs.pytest.org/en/latest/ for more information

import pytest
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import config
from src.pages.common.BasePage import BasePage


@pytest.fixture(scope="function")
def app():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield BasePage(driver)
    driver.quit()


@pytest.fixture(scope="function")
def admin_setup(app):
    """
        Login as an admin
    """
    app.go_to_site()
    app.landing.sign_up_btn.click_btn_by_css()
    app.modal.login(config.ADMIN_EMAIL, config.ADMIN_PASS)
    return app
