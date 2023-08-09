import requests
from bs4 import BeautifulSoup

BASE_URL = "https://everskies.com"
LOGIN_URL = BASE_URL + "/login-endpoint"  # Placeholder URL

class ESsession:
    def __init__(self):
        self.session = requests.Session()

    def login(self, email, password):
        login_data = {'email': email, 'password': password}
        response = self.session.post(LOGIN_URL, data=login_data)
        return "some-logout-text-or-username" not in response.text
