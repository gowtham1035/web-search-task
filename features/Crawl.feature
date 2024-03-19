Feature: Web Crawling and Page Indexing and Page Ranking

  Scenario: Web Crawling
    Given a web crawler
    When I crawl the URL "https://example.com"
    Then it should return a list of URLs

  Scenario: Page Ranking based on Query
    Given an indexer with a pre-built index
    When I score pages with the query "search query"
    Then the pages should be ranked based on relevance
    And the highest-ranked page should appear first

  Scenario: Page Indexing
    Given a indexer
    When I build index from text "This is a sample text"
    Then the inverted index should not contain the words "sample" and "text"
    And the inverted index should not contain the words "this", "is", and "a"