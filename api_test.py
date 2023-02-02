import requests
import os
from playwright.sync_api import sync_playwright
from playwright.sync_api import APIRequest
from playwright.sync_api import Playwright, APIRequestContext
#import playwright.http
'''

with sync_playwright() as p:
    url = "https://dog.ceo/api/breeds/list/all"
    browser = p.chromium.launch()
    context = browser.new_context(base_url="https://api.github.com")
    api_request_context = context.request
    page = context.new_page()
'''

def test_simple_api_test():
    with playwright.http.get("https://api.example.com/data") as response:
        assert response.status_code == 200
        print(response.json())

def simple_right_api_test():
    assert requests.get(url="https://api.example.com/data").status_code == 200