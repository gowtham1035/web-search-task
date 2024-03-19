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

