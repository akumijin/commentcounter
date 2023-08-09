from bs4 import BeautifulSoup
from collections import defaultdict

class CommentScraper:
    def __init__(self, session):
        self.session = session

    def get_comments_from_page(self, thread_url, page_num):
        url = f"{thread_url}?reply_page={page_num}"
        response = self.session.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        comments_section = soup.select('.comment')
        comments_data = []

        for comment in comments_section:
            username = comment.select_one('.username').text
            comment_text = comment.select_one('.comment-text').text  # Adjust this selector
            comments_data.append((username, comment_text))

        return comments_data
