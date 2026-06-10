import pytest
from playwright.sync_api import Page, expect

def test_mock_network_request():
    page = Page
    # 1. Intercept the fruit API call before navigating
    def handle_route(route):
        mock_data = [{"name": "Strawberry", "id": 1}]
        route.fulfill(json=mock_data)

    # Register the route handler
    page.route("*/**/api/v1/fruits", handle_route)

    # 2. Navigate to the page
    page.goto("https://demo.playwright.dev/api-mocking/")

    # 3. Assert that your mocked data rendered correctly on the UI
    expect(page.get_by_text("Strawberry")).to_be_visible()