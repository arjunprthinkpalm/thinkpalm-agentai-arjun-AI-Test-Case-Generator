"""
Page Object Model for the Login Page.
URL: https://practicetestautomation.com/practice-test-login/

This module encapsulates all interactions with the login page,
following the Page Object Model design pattern for maintainability.
"""


class LoginPage:
    """Page Object for the Practice Test Automation Login Page."""

    URL = "https://practicetestautomation.com/practice-test-login/"

    def __init__(self, page):
        """Initialize LoginPage with Playwright page instance.

        Args:
            page: Playwright page object from the browser context.
        """
        self.page = page

        # Locators
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.submit_button = page.locator("#submit")
        self.error_message = page.locator("#error")

    def navigate(self):
        """Navigate to the login page."""
        self.page.goto(self.URL, timeout=60000, wait_until="domcontentloaded")

    def enter_username(self, username: str):
        """Enter text into the username field.

        Args:
            username: The username string to enter.
        """
        self.username_input.fill(username)

    def enter_password(self, password: str):
        """Enter text into the password field.

        Args:
            password: The password string to enter.
        """
        self.password_input.fill(password)

    def click_submit(self):
        """Click the Submit button."""
        self.submit_button.click()

    def login(self, username: str, password: str):
        """Perform a complete login action.

        Args:
            username: The username to log in with.
            password: The password to log in with.
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_submit()

    def get_error_message(self) -> str:
        """Get the text of the error message displayed on failed login.

        Returns:
            The error message text.
        """
        self.error_message.wait_for(state="visible", timeout=5000)
        return self.error_message.inner_text()

    def is_error_displayed(self) -> bool:
        """Check whether an error message is visible on the page.

        Returns:
            True if the error message element is visible, False otherwise.
        """
        return self.error_message.is_visible()
