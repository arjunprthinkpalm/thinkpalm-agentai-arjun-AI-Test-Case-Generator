# AI Prompt Used to Generate Playwright Test Cases

## Model Used: Claude (Anthropic)

## Prompt:

```
You are an expert test automation engineer. I need you to generate Playwright test cases 
using Python (pytest) for the following feature.

**Feature: User Login Functionality**

**Test URL:** https://practicetestautomation.com/practice-test-login/

**Page Elements:**
- Username input field (id or label: "Username")
- Password input field (id or label: "Password")  
- Submit button (text: "Submit")

**Valid Credentials:**
- Username: student
- Password: Password123

**Test Scenarios to Cover:**

1. **Positive Test - Successful Login:**
   - Navigate to login page
   - Enter valid username "student" and password "Password123"
   - Click Submit
   - Verify URL changes to contain "logged-in-successfully"
   - Verify page displays "Congratulations" or "successfully logged in"
   - Verify "Log out" button is visible

2. **Negative Test - Invalid Username:**
   - Navigate to login page
   - Enter invalid username "incorrectUser" with valid password "Password123"
   - Click Submit
   - Verify error message "Your username is invalid!" is displayed

3. **Negative Test - Invalid Password:**
   - Navigate to login page
   - Enter valid username "student" with invalid password "incorrectPassword"
   - Click Submit
   - Verify error message "Your password is invalid!" is displayed

**Requirements:**
- Use pytest as the test framework
- Use Playwright for Python (pytest-playwright)
- Use Page Object Model (POM) design pattern
- Add proper assertions with meaningful error messages
- Add pytest markers for categorizing tests (positive/negative)
- Include docstrings for each test
- Use conftest.py for shared fixtures
- Take screenshots on test failure
- Generate an HTML report
```

## Why This Prompt Works:
1. **Specific context** — Tells the AI exactly what role to assume
2. **Clear test URL** — Provides the actual URL to test against
3. **Element details** — Specifies how to locate page elements
4. **Exact scenarios** — Describes each test case with step-by-step actions
5. **Technical requirements** — Specifies framework, patterns, and output format
6. **Best practices** — Asks for POM, fixtures, markers, and reporting
