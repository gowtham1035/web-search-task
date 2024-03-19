# from collections import defaultdict
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
# from urllib.request import urlopen
# from urllib.parse import urlparse, urljoin
# from bs4 import BeautifulSoup
# import re
# import csv

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