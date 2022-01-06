import scrapy
import csv
import os
import datetime
import json
from time import sleep

class WorksSpider(scrapy.Spider):
    name = 'works'
    download_delay = 1
    
    def __init__(self, id='', **kwargs):
        super().__init__(**kwargs)
        self.start_urls=[f'https://kakuyomu.jp/works/{id}']
        """
        try:
            with open(f'./search/{date}/herfs.csv', newline='') as f:
                reader = csv.reader(f)
                data = list(reader)
        except FileNotFoundError as error:
            print(error)
            os._exit(1)
        
        for row in data:
            for herf in row:
                self.start_urls.append(f'https://kakuyomu.jp{herf}')
        #print(self.start_urls)
        """
        
    def parse(self, response):
        work_dir = './works/' + response.url.split("/")[-1]
        #stars = response.xpath("//p[@id='workPoints']/a/span/text()").get()
        episodes = response.xpath("//li[@class='widget-toc-episode']/a/@href").extract()
        
        try:
            os.mkdir(work_dir)
        except OSError as error:
            print(error)
        
        with open(f'{work_dir}/abstract.html', 'wb') as f:
            f.write(response.body)
            
        with open(f'{work_dir}/record.json', 'w') as f:
            now = datetime.datetime.now()
            url = response.url
            data = {
                "time" : now.strftime("%Y/%m/%d, %H:%M:%S"),
                "url" : url
            }
            json.dump(data,f)
            f.write('\n')
        
        for herf in episodes:
            yield response.follow(herf, callback=self.parse_episode)
            
    def parse_episode(self, response):
        work_dir = './works/' + response.url.split("/")[-3]
        with open(f'{work_dir}/{response.url.split("/")[-1]}.html', 'wb') as f:
            f.write(response.body)
        
        with open(f'{work_dir}/record.json', 'a') as f:
            now = datetime.datetime.now()
            url = response.url
            data = {
                "time" : now.strftime("%Y/%m/%d, %H:%M:%S"),
                "url" : url
            }
            json.dump(data,f)
            f.write('\n')
    