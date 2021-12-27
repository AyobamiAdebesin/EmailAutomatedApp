import requests


class NewsFeed:
    """
    Get news from the internet
    """
    api_key = 'api_key' #get the key from NewsAPi website
    base_url = 'https://newsapi.org/v2/everything?'

    def __init__(self, interest, language):
        self.interest = interest
        self.language = language

        while self.language != 'en':
            print("Enter a correct language format")
            break

    def get(self):
        url = f"{self.base_url}" \
              f"qInTitle={self.interest}&" \
              f"language={self.language}&" \
              f"apiKey={self.api_key}"
        request = requests.get(url)
        content = request.json()
        articles = content['articles']
        email_body = "Here are some news scraped from the internet:\n\n"
        for i, article in enumerate(articles):
            email_body += '(' + str(i + 1) + ')  ' + article['title'] + '\n\t ' + article['url'] + '\n\n'

        return email_body

