import scrapy
import csv
import datetime
import json

class EpisodesSpider(scrapy.Spider):
    name = "episodes"
    allowed_domains = "kakuyomu.jp"
    
    def __init__(self, query='', path='', *args, **kwargs):
        rows = []
        super(EpisodesSpider, self).__init__(*args, **kwargs)
        with open(f'./works/{query}/herfs.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                rows.append(row)
                
        for row in rows[0]:
            url = 'https://kakuyomu.jp' + row
            self.start_urls.append(url)
            
        self.path = f'./works/{query}/episodes'
                
        with open(self.path+'/record.json', 'w') as f:
            now = datetime.datetime.now()
            url = self.start_urls
            data = {
                "time" : now.strftime("%Y/%m/%d, %H:%M:%S"),
                "url" : url
            }
            json.dump(data,f)
    
    def parse(self, response):
        filename = f'{response.url.split("/")[-1]}.html'
        with open(self.path+'/'+filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
        