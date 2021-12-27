import scrapy
import os
import csv
import datetime
import json


class SearchSpider(scrapy.Spider):
    name = "search"
    path = "./search/"        
    start_urls = ["https://kakuyomu.jp/search?total_review_point_range=10-&published_date_range=custom&published_date_start=2021-01-01&published_date_end=2021-01-02&order=published_at&page=1"]
    
    def __init__(self):
        try:
            os.mkdir(self.path)
        except OSError as error:
            print(error)
        
        
    def parse(self, response):
        works = response.xpath("//h3[@class='widget-workCard-title']/a/@href").extract()
        with open(self.path+f'{response.url.split("=")[-1]}.html', 'wb') as f:
            f.write(response.body)
            
        with open(self.path+'herfs.csv', 'a', newline='') as f:
            write = csv.writer(f)
            write.writerow(works)
        
        with open(self.path+'record.json', 'a', newline='\n') as f:
            now = datetime.datetime.now()
            url = response.url
            data = {
                "time" : now.strftime("%Y/%m/%d, %H:%M:%S"),
                "url" : url
            }
            json.dump(data,f)
            f.write('\n')
       
        nextPage = response.xpath("//p[@class='widget-pagerNext']/a/@href").get() 
        if nextPage is not None:
            if nextPage is not None:
                yield response.follow(nextPage, callback=self.parse)