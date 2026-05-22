"""
Conftest module for shared pytest fixtures.

Provides fixtures for:
- Screenshot capture on test failure
- Page object instantiation
"""
import pytest
from pages.login_page import LoginPage
from pages.success_page import SuccessPage


@pytest.fixture(scope="function")
def login_page(page):
    """Fixture that provides a LoginPage instance and navigates to it.

    Args:
        page: Playwright page fixture provided by pytest-playwright.

    Yields:
        LoginPage: An instance of the LoginPage, already navigated to the URL.
    """
    lp = LoginPage(page)
    lp.navigate()
    return lp


@pytest.fixture(scope="function")
def success_page(page):
    """Fixture that provides a SuccessPage instance.

    Args:
        page: Playwright page fixture provided by pytest-playwright.

    Returns:
        SuccessPage: An instance of the SuccessPage.
    """
    return SuccessPage(page)


# ----- Automatic screenshot on failure -----
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Pytest hook to capture a screenshot when a test fails.

    The screenshot is saved to the 'screenshots/' directory with the
    test function name as the filename.
    """
    import os

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            screenshot_dir = os.path.join(os.path.dirname(__file__), "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshot_dir, f"{item.name}.png")
            page.screenshot(path=screenshot_path)
            print(f"\n📸 Screenshot saved: {screenshot_path}")
