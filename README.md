# Test Cases Using Playwright with GitLab CI/CD

This repository contains a set of automated test cases for the website [https://www.saucedemo.com/](https://www.saucedemo.com/) implemented using Playwright. The tests cover basic scenarios for login, cart functionality, and logout.

## Project Highlights

* Test automation using Playwright — a modern end-to-end testing framework.
* Configured CI/CD pipeline in GitLab for automatic test execution on each commit.
* Detailed test cases covering key user flows.
* **Login tests for different scenarios are combined into a single parameterized test**, improving maintainability and reducing code duplication.

## Test Cases

1. **Login scenarios (parameterized test):**

   * Successful login with valid credentials
     Verifies that a user with valid username and password can successfully log in and reach the inventory page.
   * Login attempt with invalid username
     Verifies that entering a non-existent username triggers an appropriate error message.
   * Login attempt with empty username and password fields
     Verifies that leaving login fields empty results in an error message indicating the username is required.

2. **Adding a product to the cart**
   Verifies the ability to add a product to the shopping cart and see it reflected there.

3. **Logout functionality**
   Verifies that the user can successfully log out and is redirected to the login page.

## Technologies

* [Playwright](https://playwright.dev/) — browser automation framework
* GitLab CI/CD — continuous integration and delivery pipeline for automated test runs
