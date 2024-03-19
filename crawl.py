from collections import defaultdict
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from urllib.request import urlopen
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import re
import csv

class WebCrawler:
    def __init__(self):
        self.visited_urls = set()
    
    def crawl(self, url):
        if url in self.visited_urls:
            return []
        
        self.visited_urls.add(url)
        links = []
        
        try:
            html_page = urlopen(url)
            soup = BeautifulSoup(html_page, "html.parser")
            
            for link in soup.findAll('a', href=True):
                href = link.get('href')
                if href and not href.startswith('javascript:') and not href.startswith('tel:'):
                    full_url = urljoin(url, href)
                    links.append(full_url)
                
        except Exception as e:
            print("Error:", e)
        
        return links

class Indexer:
    def __init__(self):
        self.inverted_index = defaultdict(list)
        self.stop_words = set(stopwords.words('english'))
    
    def process_text(self, text):
        # Tokenize and remove stop words
        words = word_tokenize(text)
        words = [word.lower() for word in words if word.isalnum() and word.lower() not in self.stop_words]
        return words
    
    def build_index_from_text(self, text, url=None):
        words = self.process_text(text)
        
        for word in words:
            self.inverted_index[word].append(url)
    
    def get_index(self):
        return self.inverted_index

class RankingAlgorithm:
    def __init__(self, indexer):
        self.indexer = indexer
    
    def score_pages(self, query):
        query_words = set(self.indexer.process_text(query))
        index = self.indexer.get_index()
        scores = defaultdict(int)
        
        for word in query_words:
            if word in index:
                for url in index[word]:
                    scores[url] += 1
        
        return sorted(scores.items(), key=lambda x: x[1], reverse=True)

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
    input_type = input("Enter input type (url or file): ")
    input_data = input("Enter URL or file path: ")
    query = input("Enter query: ")
    main(input_type, input_data, query)
