import os

from behave import fixture, use_fixture
from splinter.browser import Browser

from pages.login_page import LoginPage
from pages.apps_page import AppsPage

from unittest import TestCase


@fixture
def browser_chrome(context):
    remote_server_url = os.environ.get("REMOTE_SERVER_URL", "http://localhost:4444/wd/hub")
    if os.environ.get('CI'):
        print("Running on CI. {sauce_username}".format(sauce_username=os.environ["SAUCE_USERNAME"]))
        remote_server_url = "http://{sauce_username}:{sauce_access_key}@localhost:4445/wd/hub".format(
            sauce_username=os.environ["SAUCE_USERNAME"],
            sauce_access_key=os.environ["SAUCE_ACCESS_KEY"]
        )
    context.browser = Browser(browser="chrome", url=remote_server_url, driver_name="remote")
    yield context.browser

    # CLEANUP
    context.browser.quit()


@fixture
def get_pages(context):
    context.pages = {
        "login": LoginPage(context.browser),
        "apps": AppsPage(context.browser),
    }
    return context.pages


def before_tag(context, tag):
    if "fixture.browser" in tag:
        use_fixture(browser_chrome, context)
        use_fixture(get_pages, context)
