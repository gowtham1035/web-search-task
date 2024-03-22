from flask import Flask, request, jsonify
from crawl import WebCrawler

app = Flask(__name__)
crawler = WebCrawler()

@app.route('/')
def index():
    return 'Welcome to the Web Search API!'

@app.route('/crawl', methods=['POST'])
def crawl():
    data = request.json
    start_url = data.get('start_url')
    if not start_url:
        return jsonify({"error": "Start URL is required"}), 400
    crawler.crawl(start_url)
    return jsonify({"message": "Crawling completed successfully!"})

@app.route('/search', methods=['GET'])
def search():
    url = request.args.get('url')
    keyword = request.args.get('keyword')
    results = crawler.search(url, keyword)
    return jsonify({"results": results})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
