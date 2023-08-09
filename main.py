from ESsession import ESsession
from ProfileScraper import ProfileScraper
from CommentScraper import CommentScraper
from collections import defaultdict

def main():
    user_comment_counts = defaultdict(int)
    all_comments = defaultdict(list)

    everskies_session = ESsession()
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if not everskies_session.login(email, password):
        print("Failed to login.")
        return

    profile_scraper = ProfileScraper(everskies_session.session)
    num_links = int(input("How many user profile links will you input? "))
    user_links = [input(f"Enter user profile link {i+1}: ") for i in range(num_links)]
    usernames_from_links = [profile_scraper.extract_username_from_profile(link) for link in user_links]

    comment_scraper = CommentScraper(everskies_session.session)
    thread_url = input("Enter the base URL of the thread (without reply_page parameter): ")
    num_pages = int(input("Enter the number of pages: "))

    for page in range(num_pages):
        comments_data = comment_scraper.get_comments_from_page(thread_url, page)
        for username, comment_text in comments_data:
            if username in usernames_from_links:
                user_comment_counts[username] += 1
                all_comments[username].append(comment_text)

    for user in usernames_from_links:
        count = user_comment_counts.get(user, 0)
        print(f"{user}: {count} comments")
        comments = all_comments.get(user, [])
        for comment in comments:
            print(f"- {comment}")
        print("\n")

if __name__ == "__main__":
    main()
