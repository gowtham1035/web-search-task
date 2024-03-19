Feature:Specific website search
    As a user, I want to search for a specific website so that I can find relevant information.

    Scenario: Indexing with URL
        Given a text "This is a sample text for domain" and an optional URL "https://example.com"
        When the index is built
        Then the inverted index should contain "domain" with URL "https://example.com"
