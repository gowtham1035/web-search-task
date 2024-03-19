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