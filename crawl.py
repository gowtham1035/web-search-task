import requests
from bs4 import BeautifulSoup
from collections import defaultdict
from urllib.parse import urljoin, urlparse

class WebCrawler:
    def __init__(self):
        self.index = defaultdict(list)
        self.visited = set()

    def crawl(self, url, base_url=None, depth=0, max_depth=4):
        if url in self.visited or depth > max_depth:
            return
        self.visited.add(url)

        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            self.index[url] = soup.get_text()

            for link in soup.find_all('a'):
                href = link.get('href')
                if href:
                    if urlparse(href).netloc:
                        href = urljoin(base_url or url, href)
                    if href.startswith(base_url or url):
                        self.crawl(href, base_url=base_url or url, depth=depth+1, max_depth=max_depth)
        except Exception as e:
            print(f"Error crawling {url}: {e}")

    def search(self, url, keyword):
        results = []
        for link, text in self.index.items():
            if url and url in link and keyword.lower() in text.lower():
                results.append(link)
        return results

    def print_results(self, results):
        if results:
            print("Search results:")
            for result in results:
                print(f"- {result}")
        else:
            print("No results found.")
