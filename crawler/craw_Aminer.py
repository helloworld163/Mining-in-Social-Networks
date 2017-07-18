#coding=utf8

from datetime import datetime
import time
import requests
from bs4 import BeautifulSoup
import random
import urllib
import json

headers = {'Host': 'api.aminer.org',
'Connection': 'keep-alive',
'Accept': 'application/json, text/plain, */*',
'Origin': 'https://cn.aminer.org',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.8,fr;q=0.6'
}


def run(name):
    data = {}
    # data['query'] = 'Yangqiu Song'
    data['query'] = name
    data['size'] = '20'
    data['sort'] = 'relevance'
    url_values = urllib.urlencode(data)
    web_name = 'https://api.aminer.org/api/search/person?' + url_values
    # print web_name
    r = requests.get(web_name, headers=headers)
    # print r.json()
    if len(r.json()['result']) > 0:
        # print r.json()['result'][0]['indices']['h_index']
        h_index = r.json()['result'][0]['indices']['h_index']
        file = open('web/%s.json' % name, 'w')
        json.dump(r.json(), file)
        file.close()
    else:
        h_index = 0
        file = open('web/wrong.txt', 'a+')
        a = "%s\n" % name
        file.write(a)
        file.close()
    return h_index


def read_name(txt_name):
    entry = []
    f = open(txt_name)
    while True:
        line = f.readline()
        if line:
            line = line.replace('\n', '')
            line = line.split(';')
            entry.append(line[0])
        else:
            break
    return entry


if __name__ == '__main__':
    name_txt = 'author_domain_id.txt'
    entry = read_name(name_txt)
    output = open('web/author_with_h_domain.txt', 'a+')
    count = 0
    # 11697
    for number in range(16203, 25000, 1):
        if count % 1000 == 0:
            print 'echo is for %d' % count
        name = entry[number]
        # name = 'Jiawei Han'
        timestr = datetime.now().strftime('%Y-%m-%d-%H')
        print 'processing at %s' % timestr
        print name
        h_value = run(name)
        print 'finish processing %s, sleep for five seconds' % timestr
        a = "%s;%d\n" % (entry[number], h_value)
        print h_value
        time.sleep(1)
        output.write(a)
        count = count + 1
    output.close()
