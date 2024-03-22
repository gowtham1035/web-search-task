import unittest
from crawl import WebCrawler

class TestWebCrawler(unittest.TestCase):
    def setUp(self):
        self.crawler = WebCrawler()

    def test_crawl_single_page(self):
        url = "http://example.com"
        self.crawler.crawl(url)
        self.assertIn(url, self.crawler.index.keys())

    def test_crawl_invalid_url(self):
        invalid_url = "http://thisisnotavalidurl123.com"
        self.crawler.crawl(invalid_url)
        self.assertNotIn(invalid_url, self.crawler.index.keys())

    def test_search_with_keyword(self):
        url = "http://example.com"
        keyword = "example"
        self.crawler.crawl(url)
        results = self.crawler.search(url, keyword)
        self.assertTrue(results)

    def test_search_without_keyword(self):
        url = "http://example.com"
        keyword = "nonexistentkeyword"
        self.crawler.crawl(url)
        results = self.crawler.search(url, keyword)
        self.assertFalse(results)

if __name__ == '__main__':
    unittest.main()
