from collections import defaultdict
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from urllib.request import urlopen
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import re
import csv

from crawl import Indexer, RankingAlgorithm, WebCrawler

# Example usage
def process_url(url):
    try:
        html_page = urlopen(url)
        soup = BeautifulSoup(html_page, "html.parser")
        text = soup.get_text()
        return text
    except Exception as e:
        print("Error:", e)
        return ""

def process_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        print("Error:", e)
        return ""

def main(input_type, input_data, query):
    crawler = WebCrawler()
    indexer = Indexer()
    ranking_algorithm = RankingAlgorithm(indexer)

    if input_type == 'url':
        links = crawler.crawl(input_data)
        for link in links:
            text = process_url(link)
            indexer.build_index_from_text(text, url=link)
    elif input_type == 'file':
        text = process_file(input_data)
        indexer.build_index_from_text(text)

    results = ranking_algorithm.score_pages(query)

    print("Search results:")
    for url, score in results:
        print(f"{url} - Score: {score}")

if __name__ == "__main__":
    input_type = "url"
    input_data = "https://example.com"
    query = "domain"
    main(input_type, input_data, query)