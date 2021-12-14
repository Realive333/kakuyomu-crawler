import scrapy

class EpisodeSpider(scrapy.Spider):
    name = "episodes"
    allowed_domains = "kakuyomu.jp"
    urls = []
    
    def __init__(self, query, *args, **kwargs):
        super(EpisodeSpider, self).__init__(*args, **kwargs)
        for item in query:
            url = 'https://kakuyomu.jp/works/' + item["works"] + '/episodes/' + item["episodes"]
            self.start_urls.append(url)
    
    def parse(self, response):
        filename = f'episode-{response.url.split("/")[-1]}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file{filename}')