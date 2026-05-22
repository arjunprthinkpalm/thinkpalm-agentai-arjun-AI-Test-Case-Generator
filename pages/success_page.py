"""
Page Object Model for the Logged-In Success Page.
URL: https://practicetestautomation.com/logged-in-successfully/

This module encapsulates interactions with the page displayed
after a successful login.
"""


class SuccessPage:
    """Page Object for the post-login success page."""

    def __init__(self, page):
        """Initialize SuccessPage with Playwright page instance.

        Args:
            page: Playwright page object from the browser context.
        """
        self.page = page

        # Locators
        self.success_message = page.locator("strong")
        self.logout_button = page.locator("a", has_text="Log out")

    def get_success_message(self) -> str:
        """Get the success message text displayed on the page.

        Returns:
            The success message text.
        """
        self.success_message.wait_for(state="visible", timeout=5000)
        return self.success_message.inner_text()

    def is_logout_visible(self) -> bool:
        """Check whether the Log out button/link is visible.

        Returns:
            True if the logout link is visible, False otherwise.
        """
        return self.logout_button.is_visible()

    def get_current_url(self) -> str:
        """Get the current page URL.

        Returns:
            The current URL string.
        """
        return self.page.url
