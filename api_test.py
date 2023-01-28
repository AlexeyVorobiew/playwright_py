import os
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    url = "https://dog.ceo/api/breeds/list/all"
    browser = p.chromium.launch()
    context = browser.new_context(base_url="https://api.github.com")
    api_request_context = context.request
    page = context.new_page()
