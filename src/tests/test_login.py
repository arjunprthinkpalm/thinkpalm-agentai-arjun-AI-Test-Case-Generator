"""
AI-Generated Playwright Test Cases for Login Functionality.

Generated using Claude AI from the feature description provided in
docs/feature_description.md using the prompt documented in docs/ai_prompt.md.

Test Categories:
- positive: Tests for successful/expected behavior
- negative: Tests for error handling and invalid input

Design Pattern: Page Object Model (POM)
Framework: pytest + pytest-playwright
"""
import pytest
import sys
from pathlib import Path

# Add src directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from pages.login_page import LoginPage
from pages.success_page import SuccessPage


# ──────────────────────────────────────────────
#  Test Data
# ──────────────────────────────────────────────
VALID_USERNAME = "student"
VALID_PASSWORD = "Password123"
INVALID_USERNAME = "incorrectUser"
INVALID_PASSWORD = "incorrectPassword"


# ══════════════════════════════════════════════
#  POSITIVE TESTS
# ══════════════════════════════════════════════
class TestSuccessfulLogin:
    """Test suite for successful login scenarios."""

    @pytest.mark.positive
    def test_successful_login_redirects_to_success_page(self, login_page, success_page):
        """
        Test Case 1: Verify successful login redirects to the correct URL.

        Steps:
            1. Navigate to the login page
            2. Enter valid username and password
            3. Click Submit
            4. Verify URL contains 'logged-in-successfully'
        """
        login_page.login(VALID_USERNAME, VALID_PASSWORD)

        # Wait for navigation to complete
        login_page.page.wait_for_url("**/logged-in-successfully/**", timeout=10000)

        current_url = success_page.get_current_url()
        assert "logged-in-successfully" in current_url, (
            f"Expected URL to contain 'logged-in-successfully', but got: {current_url}"
        )

    @pytest.mark.positive
    def test_successful_login_displays_success_message(self, login_page, success_page):
        """
        Test Case 2: Verify success page displays congratulations message.

        Steps:
            1. Navigate to the login page
            2. Enter valid credentials and submit
            3. Verify success message contains 'Congratulations' or 'successfully logged in'
        """
        login_page.login(VALID_USERNAME, VALID_PASSWORD)
        login_page.page.wait_for_url("**/logged-in-successfully/**", timeout=10000)

        message = success_page.get_success_message()
        assert "Congratulations" in message or "successfully logged in" in message, (
            f"Expected success message with 'Congratulations' or "
            f"'successfully logged in', but got: '{message}'"
        )

    @pytest.mark.positive
    def test_successful_login_shows_logout_button(self, login_page, success_page):
        """
        Test Case 3: Verify the Log out button is visible after successful login.

        Steps:
            1. Navigate to the login page
            2. Enter valid credentials and submit
            3. Verify 'Log out' button/link is visible
        """
        login_page.login(VALID_USERNAME, VALID_PASSWORD)
        login_page.page.wait_for_url("**/logged-in-successfully/**", timeout=10000)

        assert success_page.is_logout_visible(), (
            "Expected 'Log out' button to be visible on the success page, "
            "but it was not found."
        )


# ══════════════════════════════════════════════
#  NEGATIVE TESTS
# ══════════════════════════════════════════════
class TestFailedLogin:
    """Test suite for failed login scenarios."""

    @pytest.mark.negative
    def test_login_with_invalid_username_shows_error(self, login_page):
        """
        Test Case 4: Verify error message for invalid username.

        Steps:
            1. Navigate to the login page
            2. Enter an invalid username with a valid password
            3. Click Submit
            4. Verify error message: 'Your username is invalid!'
        """
        login_page.login(INVALID_USERNAME, VALID_PASSWORD)

        assert login_page.is_error_displayed(), (
            "Expected an error message to be displayed, but none was found."
        )

        error_text = login_page.get_error_message()
        assert "Your username is invalid!" in error_text, (
            f"Expected error 'Your username is invalid!', but got: '{error_text}'"
        )

    @pytest.mark.negative
    def test_login_with_invalid_password_shows_error(self, login_page):
        """
        Test Case 5: Verify error message for invalid password.

        Steps:
            1. Navigate to the login page
            2. Enter a valid username with an invalid password
            3. Click Submit
            4. Verify error message: 'Your password is invalid!'
        """
        login_page.login(VALID_USERNAME, INVALID_PASSWORD)

        assert login_page.is_error_displayed(), (
            "Expected an error message to be displayed, but none was found."
        )

        error_text = login_page.get_error_message()
        assert "Your password is invalid!" in error_text, (
            f"Expected error 'Your password is invalid!', but got: '{error_text}'"
        )

    @pytest.mark.negative
    def test_invalid_username_stays_on_login_page(self, login_page):
        """
        Test Case 6: Verify user stays on login page after invalid username.

        Steps:
            1. Navigate to the login page
            2. Enter an invalid username with a valid password
            3. Click Submit
            4. Verify the URL still contains the login page path
        """
        login_page.login(INVALID_USERNAME, VALID_PASSWORD)

        # Small wait to ensure any redirect would have happened
        login_page.page.wait_for_timeout(2000)

        current_url = login_page.page.url
        assert "practice-test-login" in current_url, (
            f"Expected to stay on login page, but URL changed to: {current_url}"
        )

    @pytest.mark.negative
    def test_invalid_password_stays_on_login_page(self, login_page):
        """
        Test Case 7: Verify user stays on login page after invalid password.

        Steps:
            1. Navigate to the login page
            2. Enter a valid username with an invalid password
            3. Click Submit
            4. Verify the URL still contains the login page path
        """
        login_page.login(VALID_USERNAME, INVALID_PASSWORD)

        # Small wait to ensure any redirect would have happened
        login_page.page.wait_for_timeout(2000)

        current_url = login_page.page.url
        assert "practice-test-login" in current_url, (
            f"Expected to stay on login page, but URL changed to: {current_url}"
        )