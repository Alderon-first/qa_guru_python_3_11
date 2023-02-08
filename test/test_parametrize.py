import pytest
from selene import have
from selene.support.shared import browser
import time


# ---- 1


@pytest.mark.parametrize('browser_open', ["390x844"], indirect=True)
def test_github_mobile_in(browser_open):
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    time.sleep(4)
    browser.element(".auth-form-header").should(have.text("Sign in to GitHub"))


@pytest.mark.parametrize('browser_open', ["1920x1080"], indirect=True)
def test_github_desktop_in(browser_open):
    browser.element(".HeaderMenu-link--sign-in").click()
    time.sleep(4)
    browser.element(".auth-form-header").should(have.text("Sign in to GitHub"))

# ---- 2


@pytest.mark.parametrize("res", [pytest.param("1920x1080", id="desktop"),
                                 pytest.param("390x844", id="mobile")])
def test_github_desktop_res(browser_open_res, res):
    if res == "390x844":
        pytest.skip(reason='Пропускаем десктопную версию в данном тесте')
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.element(".HeaderMenu-link--sign-in").click()
    time.sleep(4)
    browser.element(".auth-form-header").should(have.text("Sign in to GitHub"))


@pytest.mark.parametrize("res", [pytest.param("1920x1080", id="desktop"),
                                 pytest.param("390x844", id="mobile")])
def test_github_mobile_res(browser_open_res, res):
    if res == "1920x1080":
        pytest.skip(reason='Пропускаем мобильную версию в данном тесте')
    browser.config.window_width = 390
    browser.config.window_height = 844
    browser.element(".HeaderMenu-link--sign-in").click()
    time.sleep(4)
    browser.element(".auth-form-header").should(have.text("Sign in to GitHub"))
