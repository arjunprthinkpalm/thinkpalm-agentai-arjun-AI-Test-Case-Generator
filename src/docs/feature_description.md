# Feature Description: User Login Functionality

## Overview
The application provides a user login page that allows registered users to authenticate 
and access their dashboard. The login page is accessible at a public URL and contains 
a standard username/password form.

## Feature Details

### Login Page (URL: https://practicetestautomation.com/practice-test-login/)

**Elements:**
- **Username field**: A text input field where users enter their username
- **Password field**: A password input field where users enter their password  
- **Submit button**: A button labeled "Submit" that submits the login form

**Valid Credentials:**
- Username: `student`
- Password: `Password123`

### Expected Behaviors:

#### Successful Login:
1. User navigates to the login page
2. User enters valid username (`student`) and password (`Password123`)
3. User clicks the Submit button
4. User is redirected to a success page (URL contains `practicetestautomation.com/logged-in-successfully/`)
5. Success page displays a message containing "Congratulations" or "successfully logged in"
6. A "Log out" button/link is visible on the success page

#### Failed Login (Invalid Username):
1. User navigates to the login page
2. User enters an invalid username (e.g., `incorrectUser`) with a valid password (`Password123`)
3. User clicks the Submit button
4. User remains on the login page (URL does not change)
5. An error message is displayed: "Your username is invalid!"

#### Failed Login (Invalid Password):
1. User navigates to the login page
2. User enters a valid username (`student`) with an invalid password (e.g., `incorrectPassword`)
3. User clicks the Submit button
4. User remains on the login page (URL does not change)
5. An error message is displayed: "Your password is invalid!"

## Test Scenarios to Cover

### Positive Tests
- ✅ Successful login redirects to success page
- ✅ Success page displays congratulations message
- ✅ Log out button is visible after successful login

### Negative Tests
- ✅ Invalid username shows error message
- ✅ Invalid password shows error message
- ✅ User stays on login page after invalid username
- ✅ User stays on login page after invalid password

## Assumptions
- The application is always accessible at the provided URL
- Network connectivity is stable
- Only one browser tab/session is active during testing
- Test data (valid credentials) does not change between test runs
