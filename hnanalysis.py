# -*- coding: utf-8 -*-

### This script removes posts with 0 comments then samples 20,000 for analysis###

### Import source data file
import csv

hn_full = []

with open('hacker_news_source.csv', encoding='utf8') as csv_file:
    read_file = csv.reader(csv_file, delimiter = ',')
    for row in read_file:
        hn_full.append(row)

headers = hn_full[0]
hn_full = hn_full[1:]


### Remove posts with 0 comments
hn_comments = []

for post in hn_full:
    comments = int(post[4])
    if comments > 0:
        hn_comments.append(post)


### Randomly sample 20,000 posts for analysis
from random import sample
hn = sample(hn_comments,20000)


### Write sampled data into new file for analysis
with open('hacker_news.csv', 'w', newline='', encoding='utf8') as sample_file:
    write_file = csv.writer(sample_file, delimiter=',')
    write_file.writerow(headers)
    for post in hn:
        write_file.writerow(post)

        
        