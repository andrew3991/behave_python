from behave import *
use_step_matcher("re")



@given("I open start activity")
def step_impl(context):
    context
    start = context.driver.find_element_by_id('ru.appkode.friendsclub.internal:id/welcome_controller_phone_button')
    try:
        assert start.is_displayed() is True
    except AssertionError as error:
        error.args += ('Activity didn`t start',)
        raise



@when("I enter number (\d+)")
def step_impl(context, search_term):
    context.search_term = search_term
    vhod = context.driver.find_element_by_id('ru.appkode.friendsclub.internal:id/welcome_controller_phone_button')
    vhod.click()
    phone = context.driver.find_element_by_id('ru.appkode.friendsclub.internal:id/phone_input_edit_text')
    phone.send_keys("'" + search_term + "'")
    try:
        assert phone.is_enabled() is True
    except AssertionError as error:
        error.args += ('Phone is disable',)
        raise
    #raise NotImplementedError(u'STEP: When I enter number 9114585525')


@then("Button is active")
def step_impl(context):
    button = context.driver.find_element_by_id('ru.appkode.friendsclub.internal:id/progress_button_button')
    try:
        assert button.is_enabled() is True
    except AssertionError as error:
        error.args += ('Button is disable',)
        raise
    #raise NotImplementedError(u'STEP: Then Button is active')