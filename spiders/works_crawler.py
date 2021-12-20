import scrapy
import os
import csv
import datetime
import json

class WorksSpider(scrapy.Spider):
    name = "works"
    allowed_domains = "kakuyomu.jp"
    
    def __init__(self, query='', path='', *args, **kwargs):
        super(WorksSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['https://kakuyomu.jp/works/' + query]
        self.path = './works/' + query
        try:
            os.mkdir(path)
        except OSError as error:
            print(error)
        
    def parse(self, response):
        stars = response.xpath("//p[@id='workPoints']/a/span/text()").get()
        episodes = response.xpath("//li[@class='widget-toc-episode']/a/@href").extract()
            
        with open(self.path+'/abstract.html', 'wb') as f:
            f.write(response.body)
        
        with open(self.path+'/herfs.csv', 'w') as f:
            write = csv.writer(f)
            write.writerow(episodes)
            
        with open(self.path+'/record.json', 'w') as f:
            now = datetime.datetime.now()
            url = self.start_urls
            data = {
                "time" : now.strftime("%Y/%m/%d, %H:%M:%S"),
                "url" : url
            }
            json.dump(data,f)
        
        self.log(f'saved file {self.path}')