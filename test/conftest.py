import pytest
from selene.support.shared import browser


@pytest.fixture(scope="function", autouse=True, params=[pytest.param("1920x1080", id="desktop"),
                                                        pytest.param("390x844", id="mobile")])
def browser_open(request):
    if request.param == "1920x1080":
        browser.config.window_width = 1920
        browser.config.window_height = 1080
    else:
        browser.config.window_width = 390
        browser.config.window_height = 844
    browser.open('https://github.com')
    yield
    browser.quit()
