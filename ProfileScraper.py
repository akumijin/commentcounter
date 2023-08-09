from bs4 import BeautifulSoup

class ProfileScraper:
    def __init__(self, session):
        self.session = session

    def extract_username_from_profile(self, user_link):
        response = self.session.get(user_link)
        soup = BeautifulSoup(response.text, 'html.parser')
        username = soup.select_one('.profile-username-selector').text  # Placeholder selector
        return username.strip()
