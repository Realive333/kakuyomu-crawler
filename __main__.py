import os

def main():
    try:
        os.mkdir('search')
    except OSError as error:
        print(error)
    
    try:
        os.mkdir('works')
    except OSError as error:
        print(error)
        
    os.system('scrapy crawl search -a year=2021 -a month=10')
    
if __name__ == '__main__':
    main()