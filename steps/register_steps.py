from behave import *
from pages.registration_page import RegistrationPage
from utils.webdriver import initialize_webdriver


@given("User is in the Home Page")
def step_given_user_on_home_page(context):
    context.driver = initialize_webdriver()
    context.registration_page = RegistrationPage(context.driver)
    context.driver.get("http://www.automationpractice.pl/index.php")
    registration_page = context.registration_page
    registration_page.verify_home_page()
    context.feature_name = context.feature.name


@when("User click sign in button")
def step_when_user_click_sign_in_button(context):
    registration_page = context.registration_page
    registration_page.click_sign_in_button()


#
@when("User input email in registration field")
def step_when_user_submits_registration_form(context):
    registration_page = context.registration_page
    registration_page.enter_registration_details()


@when("User click submit button")
def step_then_user_successfully_registered(context):
    registration_page = context.registration_page
    registration_page.submit_registration_form()
    pass


@when("User input personal information in registration field")
def step_then_user_successfully_registered(context):
    registration_page = context.registration_page
    registration_page.input_personal_info_form("Example", "Test", "12341234")
    pass


@when("User submit personal information '{condition}' newsletter")
def step_then_user_submit_personal_info(context, condition):
    registration_page = context.registration_page
    registration_page.submit_personal_info(condition)
    pass


@then("User can see toast success in My Account page")
def step_then_user_in_my_account_page(context):
    registration_page = context.registration_page
    registration_page.my_account_page()
    pass
