from behave import given, when, then


@given('main page is open')
def step_impl(context):
    context.driver.get(context.base_url)


@when('click on "Dexcom CLARITY for Home Users" button')
def click_home_users_button(context):
    context.main_page.click_home_user_button()


@when('enter correct username')
def input_username(context):
    context.login_page.set_username(context.username)


@when('enter correct password')
def input_password(context):
    context.login_page.set_password(context.password)


@when('click on login button')
def click_login(context):
    context.login_page.click_login_button()


@then('login successfully')
def validate_loggin(context):
    current_url = context.driver.current_url
    expected_url = "https://clarity.dexcom.com/"
    assert current_url == expected_url, f"URL actual: {current_url} != URL esperada: {expected_url}"