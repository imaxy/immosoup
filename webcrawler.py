import requests
from bs4 import BeautifulSoup

# Website class for handling the links
class LinkManager:
    def __init__(self, page_url, prefix_url, query):
        self.prefix_url = prefix_url
        self.page_url = page_url
        self.webpage = requests.get(page_url)
        self.soup = BeautifulSoup(self.webpage.text, 'html.parser')
        self.links = []
        app_links = self.soup.find_all("div", query)

        for el in app_links:
            children = el.findChildren("a", recursive=False)
            for a in children:
                self.links.append(self.prefix_url + a.attrs['href'])