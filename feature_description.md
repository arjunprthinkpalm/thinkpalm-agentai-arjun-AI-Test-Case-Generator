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

#### Failed Login - Invalid Username:
1. User navigates to the login page
2. User enters an invalid username (e.g., `incorrectUser`) and valid password (`Password123`)
3. User clicks the Submit button
4. An error message is displayed: "Your username is invalid!"
5. User remains on the login page

#### Failed Login - Invalid Password:
1. User navigates to the login page
2. User enters a valid username (`student`) and invalid password (e.g., `incorrectPassword`)
3. User clicks the Submit button
4. An error message is displayed: "Your password is invalid!"
5. User remains on the login page

## Notes
- This is a practice test automation site designed for learning
- No real user data is involved
- The site is publicly accessible and free to use for testing
