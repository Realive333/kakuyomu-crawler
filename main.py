import spiders.episode_crawler as episode
import spiders.works_crawler as work
import os
from scrapy.crawler import CrawlerProcess

def main():
    
    try:
        os.mkdir('data')
    except OSError as error:
        print(error)
            
    process = CrawlerProcess({
    })
    dicts = [
        {"works": "1177354054880238351", "episodes":"1177354054880238419"},
        {"works": "1177354054880238351", "episodes":"1177354054880289448"}
    ]
    
    process.crawl(work.WorkSpider, query='1177354054880238351')
    #process.crawl(episode.EpisodeSpider, query=dicts)
    process.start()
    
if __name__ == '__main__':
    main()