while IFS=, read -r col
do
    scrapy crawl works -a id=$col
done < ./search/$1/herfs.dat

#awk -F, 'BEGIN{OFS="\n"}{$1=$1;print}' ./search/$1/herfs.dat
