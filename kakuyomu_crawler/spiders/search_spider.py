import scrapy
import os
import csv
import datetime
import json
import calendar
from time import sleep

def getStartURL(year, month):
    try:
        intYear = int(year)
        intMonth = int(month)
    except TypeError:
        print(f'Error while casting str to int: {year}-{month}')
    startDate = f'{year}-{month}-01'
    endDate = f'{year}-{month}-{calendar.monthrange(intYear, intMonth)[1]}'
    return [f'https://kakuyomu.jp/search?total_review_point_range=10-&published_date_range=custom&published_date_start={startDate}&published_date_end={endDate}&order=published_at&page=1']

class SearchSpider(scrapy.Spider):
    download_delay = 1
    name = "search"
    path = "./search/"        
    
    def __init__(self, year='2021', month='12', **kwargs):
        super().__init__(**kwargs)
        self.path = f'./search/{year}-{month}/'
        try:
            os.mkdir(self.path)
        except OSError as error:
            print(error)
            
        self.start_urls = getStartURL(year, month)
        
        
    def parse(self, response):
        works = response.xpath("//h3[@class='widget-workCard-title']/a/@href").extract()
        with open(self.path+f'{response.url.split("=")[-1]}.html', 'wb') as f:
            f.write(response.body)
            
        with open(self.path+'herfs.dat', 'a', newline='') as f:
            for r in works:
                f.write(f'{r}\n')
            """
            write = csv.writer(f)
            for r in works:
                write.writerow(r)
            """
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
            yield response.follow(nextPage, callback=self.parse) 