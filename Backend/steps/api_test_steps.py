import requests
from dotenv import load_dotenv
from behave import given, when, then
import os
load_dotenv()

session = requests.Session()

@given('the API URL is "{url}"')
def step_impl(context, url):
    context.url = url


@when('have valid AuthToken')
def step_impl(context):
    context.authtoken = os.getenv('AUTHTOKEN')
    context.headers = {'Authorization': 'Bearer ' + context.authtoken}


@when('POST request is sended')
def step_impl(context):
    context.response = session.post(context.url, headers=context.headers)


@then(u'response code is 200')
def step_impl(context):
    assert context.response.status_code == 200


@then(u'analysisSessionId is not null')
def step_impl(context):
    assert context.response.json()["analysisSessionId"] is not None, "analysisSessionId should not be null"