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

---

## Manual Test Cases Generator Prompt

### Model Used: Claude (Anthropic)

### Prompt:

```
You are an expert QA test analyst and documentation specialist. I need you to generate 
comprehensive manual test cases for the following feature/functionality in markdown format.

**Feature: [Feature Name]**

**Feature Description:**
[Provide detailed description of the feature, what it does, and its purpose]

**User Story/Acceptance Criteria:**
- [Criteria 1]
- [Criteria 2]
- [Criteria 3]

**Scope:**
- In Scope: [What should be tested]
- Out of Scope: [What should NOT be tested]

**Test Environment:**
- Browser/OS: [Specify test environment details]
- Test Data Available: [Yes/No and what data]
- Dependencies: [Any external dependencies or prerequisites]

**Requirements for Test Cases:**
- Generate test cases in markdown table format with columns: TC ID, Test Case Title, 
  Preconditions, Test Steps, Expected Result, Test Type (Positive/Negative/Edge Case)
- Each test case should have clear, numbered steps
- Include both positive (happy path) and negative scenarios
- Add edge cases and boundary value tests
- Provide realistic test data examples
- Group related test cases logically by feature area
- Add priority/severity levels (P0/P1/P2)
- Include expected vs actual result columns

**Output Format:**
```
# [Feature Name] - Manual Test Cases

## Test Case Summary
- Total Test Cases: [Number]
- Positive Test Cases: [Number]
- Negative Test Cases: [Number]
- Edge Cases: [Number]

## Test Case Details

### Category: [Category Name]

| TC ID | Test Case Title | Preconditions | Test Steps | Expected Result | Test Type | Priority |
|-------|-----------------|---------------|-----------|-----------------|-----------|----------|
| TC-001 | [Title] | [Preconditions] | 1. [Step 1]<br>2. [Step 2]<br>3. [Step 3] | [Expected Result] | Positive | P0 |
```

- Ensure test cases are independent and can be executed in any order
- Add notes section for complex scenarios or known issues
- Provide clear pass/fail criteria for each test case
```

### Why This Prompt Works:
1. **Clear role definition** — Tells AI to act as QA analyst and documentation specialist
2. **Structured format** — Specifies markdown table format for easy tracking
3. **Comprehensive coverage** — Requests positive, negative, and edge case scenarios
4. **Test classification** — Includes priority levels and test types for better organization
5. **Detailed steps** — Requests numbered steps with clear preconditions and expected results
6. **Realistic output** — Generates production-ready test case documentation
7. **Scope definition** — Clearly defines what should and shouldn't be tested
