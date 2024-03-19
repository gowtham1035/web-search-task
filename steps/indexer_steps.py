from behave import given, when, then
from crawl import Indexer

# ** Behave scenario examples (assuming a feature file)

# Scenario: Indexing with URL
#   Given a text "This is a sample text for indexing" and an optional URL "https://example.com"
#   When the index is built
#   Then the inverted index should contain "indexing" with URL "https://example.com"

# Scenario: Indexing without URL
#   Given a text "This is another sample text"
#   When the index is built
#   Then the inverted index should contain "text"  # No URL check for this scenario

class IndexerTests:

    @given('a text "{text}" and an optional URL "{url}"')
    def create_text_and_url(self, text, url=None):
        self.text = text
        self.url = url

    @when('the index is built')
    def build_index(self):
        self.indexer = Indexer()
        self.indexer.build_index_from_text(self.text, self.url)

    @then('the inverted index should contain "{word}" with URL "{url}"')
    def check_index_with_url(self, word, url):
        print("Index content:", self.indexer.get_index())
        assert word in self.indexer.get_index(), f"Word '{word}' not found in the index."
        assert url in self.indexer.get_index()[word], f"Word '{word}' not found in index with URL '{url}'"
