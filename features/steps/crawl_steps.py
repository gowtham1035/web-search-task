# -- FILE: features/steps/web_crawler_steps.py
from behave import given, when, then
from crawl import *

@given('a web crawler')
def step_given_web_crawler(context):
    context.web_crawler = WebCrawler()

@when('I crawl the URL "{url}"')
def step_when_crawl_url(context, url):
    context.crawled_urls = context.web_crawler.crawl(url)

@then('it should return a list of URLs')
def step_then_return_list_of_urls(context):
    assert isinstance(context.crawled_urls, list)
    assert all(isinstance(url, str) for url in context.crawled_urls)

@then('it should not return any URLs')
def step_then_not_return_any_urls(context):
    assert len(context.crawled_urls) == 0

@given('an indexer with a pre-built index')
def step_given_indexer_with_pre_built_index(context):
    context.indexer = Indexer()
    context.indexer.build_index_from_text("Sample text for indexing", "https://example.com")

@when('I score pages with the query "{query}"')
def step_when_score_pages_with_query(context, query):
    context.results = RankingAlgorithm(context.indexer).score_pages(query)

@then('the pages should be ranked based on relevance')
def step_then_pages_ranked_based_on_relevance(context):
    # Add assertions to check if pages are ranked based on relevance
    pass

@then('the highest-ranked page should appear first')
def step_then_highest_ranked_page_appears_first(context):
    # Add assertions to check if the highest-ranked page appears first
    pass

@then('no pages should be returned')
def step_then_no_pages_returned(context):
    # Add assertions to check if no pages are returned
    pass
# -- FILE: features/steps/indexer_steps.py
from behave import given, when, then
from crawl import Indexer

@given('a indexer')
def step_impl(context):
    context.indexer = Indexer()

@when('I build index from text "{text}"')
def step_when_build_index_from_text(context, text):
    context.indexer.build_index_from_text(text)

@then('the inverted index should contain the words "{words}"')
def step_then_inverted_index_contains_words(context, words):
    words_list = words.split()
    inverted_index = context.indexer.get_index()
    for word in words_list:
        assert word in inverted_index

@then('the inverted index should not contain the words "{words}"')
def step_then_inverted_index_not_contains_words(context, words):
    words_list = words.split()
    inverted_index = context.indexer.get_index()
    for word in words_list:
        assert word not in inverted_index

@then('the inverted index should be empty')
def step_then_inverted_index_empty(context):
    inverted_index = context.indexer.get_index()
    assert len(inverted_index) == 0
