Feature: RankingAlgorithm score_pages method

  Scenario: Score pages based on query
    Given an indexer with a pre-built index
    When I score pages with the query "search query"
    Then the pages should be sorted by score in descending order
    And the highest-scoring page should be listed first
