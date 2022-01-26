echo "kakuyomu_crawler search_ss shell script start"
for YYYY in `seq 2022 2022`
do
  for MM in `seq 1 1`
  do
    echo "crawling... year=$YYYY month=$MM"
    scrapy crawl search -a year=$YYYY -a month=$MM
  done
done

