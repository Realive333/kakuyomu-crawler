## File Hireachy
```
/kakuyomi_crawler
  |------/kakuyomu_crawler              //クローラーの実行ファイル
  |       ...           
  |
  |------/search
  |       |------/2021-12
  |       |       |------herfs.dat      //クロールしたリンク (e.g./works/16816927859450962735)
  |       |       |------record.json    //クロール履歴記録
  |       |       |------1.html         //html記録
  |       |        ...
  |        ...
  |
  |------/works
  |       |------/16816927859450962735
  |       |       |------record.json   //クロール履歴記録
  |       |       |------abstract.html //html記録(作品概要)
  |       |       |------1.html        //html記録(本文)
  |       |        ...
  |        ...
  |
  |------search_ss.sh                  //search spider用shell script
  |------works_ss.sh                   //works spider用shell script
```
## 手順
1. `/search`と`/works`フォルダを作り出す
    - `mkdir search works`
2. search spiderを起動して、月ごとに作品のリンクを取得する
    - `bash search_ss.sh`
3. works spiderを起動して、`/search`フォルダ内の`herfs.csv`にあったリンクから各作品をクロールする
    - `bash works_ss.sh {2021-12}`

## Spiderの仕様
### search spider
- 年分と月分を指定して、当月の作品のリンクをクロールする
    - e.g. `scrapy crawl search -a year={2021} -a month={12}`
### works spider
- 作品idを指定して、該当の作品の概要と本文をクロールする
    - e.g. `scrapy crawl works scrapy crawl works -a id={/works/16816927859450962735}`

## Shell Scriptの仕様
### search_ss.sh
- 開始年・終了年及び開始月・終了月を指定できます
```sh
for YYYY in `seq {2021 2021}`
do
    for MM in `seq {12 12}`
    do
        echo "crawling... year=$YYYY month=$MM"
        scrapy crawl search -a year=$YYYY -a month=$MM
    done
done
```
### works_ss.sh
- フォルダ名をパラメーターとして入力し、当月の作品をクロールする
```sh
while IFS=, read -r col
do
    scrapy crawl works -a id=$col
done < ./search/$1/herfs.dat
```
## 出力の仕様
### /search
- 各フォルダは`年分-月分`のようで命名します
- htmlファイル
    - 実際クロールした検索ページのデータ
- .datファイル
    - 目標のリンク資料
 ```herfs.dat
      /works/16816927859450962735
      /works/16816927859388212664
      /works/16816927859450842794
      /works/16816927859450543447
      /works/16816927859450451545
      /works/16816927859448348979
      /works/16816927859448671773
      ...
```
- .jsonファイル
  - スパイダーのクロール記録
```record.json
{"time": "2022/01/20, 12:28:49", "url": "https://kakuyomu.jp/search?total_review_point_range=10-&published_date_range=custom&published_date_start=2021-12-01&published_date_end=2021-12-31&order=published_at&page=1"}
{"time": "2022/01/20, 12:28:50", "url": "https://kakuyomu.jp/search?total_review_point_range=10-&published_date_range=custom&published_date_start=2021-12-01&published_date_end=2021-12-31&order=published_at&page=2"}
{"time": "2022/01/20, 12:28:51", "url": "https://kakuyomu.jp/search?total_review_point_range=10-&published_date_range=custom&published_date_start=2021-12-01&published_date_end=2021-12-31&order=published_at&page=3"}
...
```

### /works
- 各作品のIDでフォルダを命名します
- htmlファイル
    - 目標のデータ
        - `abstract`で出力して、概要のデータ
        - `ページID`で出力して、本文のデータ
- .jsonファイル
    - スパイダーのクロール記録
```record.json
{"time": "2022/01/20, 12:33:09", "url": "https://kakuyomu.jp/works/16816927859434545029", "episodes": ["/works/16816927859434545029/episodes/16816927859434561388", "/works/16816927859434545029/episodes/16816927859458623550", "/works/16816927859434545029/episodes/16816927859475221042", "/works/16816927859434545029/episodes/16816927859514345620", "/works/16816927859434545029/episodes/16816927859544521136", "/works/16816927859434545029/episodes/16816927859577023624"]}

```