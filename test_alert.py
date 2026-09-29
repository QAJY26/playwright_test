import re
import pytest
from playwright.sync_api import Page, expect

# Slow down the browser for debugging
@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "slow_mo": 2000,
    }

# Test different types of JavaScript alerts
def test_javascript_alerts(page: Page):
    page.goto('https://the-internet.herokuapp.com/javascript_alerts')

    # Scenario 1: Test basic alert button
    page.get_by_role("button", name="Click for JS Alert").click()
    expect(page.locator("#result")).to_have_text("You successfully clicked an alert")

    # Scenario 2: Test confirmation button and click Cancel
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Click for JS Confirm").click()
    expect(page.locator("#result")).to_have_text("You clicked: Cancel")

    # Scenario 3: Test prompt button by typing text and clicking OK
    page.once("dialog", lambda dialog: dialog.accept("Hello Playwright"))
    page.get_by_role("button", name="Click for JS Prompt").click()
    expect(page.locator("#result")).to_have_text("You entered: Hello Playwright")
