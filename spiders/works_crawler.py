import scrapy
import os
import csv

class WorkSpider(scrapy.Spider):
    name = "works"
    allowed_domains = "kakuyomu.jp"
    
    def __init__(self, query='', *args, **kwargs):
        super(WorkSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['https://kakuyomu.jp/works/' + query]
        
    def parse(self, response):
        title = response.css('title::text').get()
        stars = response.xpath("//p[@id='workPoints']/a/span/text()").get()
        episodes = response.xpath("//li[@class='widget-toc-episode']/a/@href").extract()
        
        try:
            os.mkdir('./data/'+title)
        except OSError as error:
            print(error)
            
        with open('./data/'+title+'/abstract.html', 'wb') as f:
            f.write(response.body)
        f.close()
        
        with open('data/'+title+'/herfs.csv', 'w') as f2:
            write = csv.writer(f2)
            write.writerow(episodes)
        f2.close()
        
        self.log(f'saved file {title}')