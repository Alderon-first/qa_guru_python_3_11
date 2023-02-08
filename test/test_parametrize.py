import pytest
from selene import have
from selene.support.shared import browser
import time


# ----параметризация тестов


@pytest.mark.parametrize('browser_open', ["390x844"], indirect=True)
def test_github_mobile_in(browser_open):
    browser.element(".d-inline-block").click()
    browser.element('color-fg-on-emphasis').click()
    time.sleep(2)
    browser.element(".auth-form-header").should(have.text("Sign in to GitHub"))


@pytest.mark.parametrize('browser_open', ["1920x1080"], indirect=True)
def test_github_desktop_in(browser_open):
    browser.element(".HeaderMenu-link--sign-in").click()
    time.sleep(2)
    browser.element(".auth-form-header").should(have.text("Sign in to GitHub"))

# ---- параметризация фикстуры
