import os
import spiders.works_crawler as works
import spiders.episodes_crawler as episodes
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from twisted.internet import reactor, defer

class Traveler:
    def __init__(self, query):
        self.query = query
    
    def travasal(self):
        try:
            os.mkdir(f'./works/{self.query}')
        except OSError as error:
            print(error)
        
        try:
            os.mkdir(f'./works/{self.query}/episodes')
        except OSError as error:
            print (error)
            
        configure_logging()
        runner = CrawlerRunner()
        
        @defer.inlineCallbacks
        def crawl():
            yield runner.crawl(works.WorksSpider, query=self.query)
            yield runner.crawl(episodes.EpisodesSpider, query=self.query)
            reactor.stop()
            
        crawl()
        reactor.run()