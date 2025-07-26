import pytest
from locators import *

@pytest.mark.parametrize(
    "username, password, expected_url_part, expected_error",
    [
        ("standard_user", "secret_sauce", "/inventory.html", None),
        ("invalid_user", "secret_sauce", None, "Username and password do not match"),
        ("", "", None, "Username is required"),
    ]
)
def test_login_scenarios(page, base_url, username, password, expected_url_part, expected_error):
    page.goto(base_url)
    page.fill(LOGIN_USERNAME_INPUT, username)
    page.fill(LOGIN_PASSWORD_INPUT, password)
    page.click(LOGIN_BUTTON)
    if expected_url_part:
        assert expected_url_part in page.url
    elif expected_error:
        error = page.locator(LOGIN_ERROR_MESSAGE)
        assert error.is_visible()
        assert expected_error in error.text_content()


def test_add_item_to_cart(page, base_url, valid_credentials):
    page.goto(base_url)
    page.fill(LOGIN_USERNAME_INPUT, valid_credentials["username"])
    page.fill(LOGIN_PASSWORD_INPUT, valid_credentials["password"])
    page.click(LOGIN_BUTTON)
    page.click(INVENTORY_ADD_TO_CART_BUTTON)
    page.click(CART_LINK)
    assert page.locator(CART_ITEM).count() == 1


def test_logout(page, base_url, valid_credentials):
    page.goto(base_url)
    page.fill(LOGIN_USERNAME_INPUT, valid_credentials["username"])
    page.fill(LOGIN_PASSWORD_INPUT, valid_credentials["password"])
    page.click(LOGIN_BUTTON)
    page.click(MENU_BUTTON)
    page.wait_for_selector(LOGOUT_LINK, state="visible")
    page.click(LOGOUT_LINK)
    assert base_url in page.url
    assert page.locator(LOGIN_BUTTON).is_visible()
