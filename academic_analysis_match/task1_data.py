import numpy as np
from datetime import datetime
import time
import requests
from bs4 import BeautifulSoup
import random


def read_data(txt_name):
    f = open(txt_name)
    entry = {}
    count = 0
    while True:
        if count >= 100:
            break
        line = f.readline()
        if line == '\n':
            entry[author_name] = {}
            entry[author_name]['author_id'] = author_id
            entry[author_name]['author_org'] = author_org
            entry[author_name]['author_url'] = author_url
            count += 1
            continue
        if line:
            line = line.strip()
            if line[0:4] == '#id:':
                author_id = line[4:len(line)]
            if line[0:6] == '#name:':
                author_name = line[6:len(line)]
            if line[0:5] == '#org:':
                author_org = line[5:len(line)]
            if line[0:21] == '#search_results_page:':
                author_url = line[21:len(line)]
        else:
            break
    return entry


def get_web(web_name):
    r = requests.get(web_name)
    soup = BeautifulSoup(r.content, "lxml")
    # print soup.prettify()
    soup_target = soup.select('h3 a')
    # print soup_target
    if len(soup_target) > 1:
        index = random.randint(0, 1)
        href = soup_target[index]
    elif len(soup_target) <= 0:
        return 0
    website = href.get('href')
    return website

if __name__ == '__main__':
    train_txt_name = 'data/task1/training.txt'
    entry = read_data(train_txt_name)
    count = 0
    wrong = []
    name_web = {}
    for name in entry.keys():
        if count >= 10:
            break
        count += 1
        data_url = entry[name]['author_url']
        website = get_web(data_url)
        print website
        if website == 0:
            wrong.append(name)
        else:
            name_web[name] = website
    print name_web
    print wrong



