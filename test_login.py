import pytest
import re
from playwright.sync_api import Page, expect

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "slow_mo": 1500,  # 1.5-second delay before every browser action
    }

def test_has_title(page: Page):
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

    page.get_by_placeholder('Username').fill('Admin')
    page.get_by_placeholder('Password').fill('admin123')
    page.get_by_role('button', name='Login').click()
    page.get_by_title("Help").click()
    page.get_by_alt_text("profile picture").click()
    page.get_by_text("Logout").click()

# page.get_by_role()         -> Use to find structural web components like buttons, checkboxes, headings, or links by their functional purpose.
# page.get_by_text()         -> Use when you want to find an element solely by the literal, visible text content it displays on the screen.
# page.get_by_label()        -> Use to target form input fields by matching the text of the HTML label associated with them.
# page.get_by_placeholder()  -> Use for input boxes that have no structural label but display faint, grey hint text inside them.
# page.get_by_alt_text()     -> Use to locate images, logos, or avatars by their descriptive alternative text attribute.
# page.get_by_title()        -> Use when an element reveals extra details via an HTML title attribute tooltip when hovered over.
# page.get_by_test_id()      -> Use as a reliable fallback when developers add dedicated data-testid attributes specifically for testing.