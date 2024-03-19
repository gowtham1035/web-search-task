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

class Indexer:
    # Inverted index (words -> document URLs)
    def __init__(self):
        self.inverted_index = defaultdict(list)
        # Stop words from NLTK (assumed imported)
        self.stop_words = set(stopwords.words('english'))

    # Clean and normalize text (lowercase, alnum, remove stop words)
    def process_text(self, text):
        words = word_tokenize(text)
        words = [word.lower() for word in words if word.isalnum() and word.lower() not in self.stop_words]
        return words

    # Build index from text, optionally associate URL
    def build_index_from_text(self, text, url=None):
        words = self.process_text(text)
        for word in words:
            self.inverted_index[word].append(url)

    # Get the built inverted index
    def get_index(self):
        return self.inverted_index
