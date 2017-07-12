#coding=utf8
'''
'''

from datetime import datetime
import time
import requests
from bs4 import BeautifulSoup
from str_util import unicode2str

res_dir = 'res/'


def sort_by_reply(res):
    return sorted(res, key=lambda d:int(d[1]), reverse=True)


def sort_by_view(res):
    return sorted(res, key=lambda d:int(d[2]), reverse=True)


def sort_by_reply_by_view(res):
    res = sorted(res, key=lambda d:float(d[3]), reverse=True)
    return [r for r in res if int(r[2]) > 1000]


def save_res(filename, res):
    fw = open(res_dir + filename, 'w+')
    fw.write('\n'.join(['\t'.join(r) for r in res]))


def run(timestr):
    r = requests.get('http://bbs.hupu.com/bxj')
    soup = BeautifulSoup(r.content, "lxml")
    ps = soup.find_all(id='pl')[0].find_all('tr')

    res = []
    for l in ps[1:]:
        #print l
        title = l.find_all('td', class_='p_title')[0].text.split()[0]
        info = l.find_all('td', class_='p_re')[0].text
        reply, view = info.split('/')
        reply = reply.strip()
        view = view.strip()
        url_id = l.get('mid')
        if int(view) < 10:
            continue
        res.append((unicode2str(title), unicode2str(reply), unicode2str(view), str(round(float(reply)/float(view),3)), unicode2str(url_id)))
    res = sort_by_view(res)
    wfilename = 'res_by_view-%s.txt' % timestr
    save_res(wfilename, res)

    res = sort_by_reply(res)
    wfilename = 'res_by_reply-%s.txt' % timestr
    save_res(wfilename, res)

    res = sort_by_reply_by_view(res)
    wfilename = 'res_by_reply_by_view.txt'
    wfilename = 'res_by_reply-by_view-%s.txt' % timestr
    save_res(wfilename, res)

if __name__ == '__main__':
    while True:
        timestr = datetime.now().strftime('%Y-%m-%d-%H')
        print 'processing at %s' % timestr
        run(timestr)
        print 'finish processing %s, sleep for one hour' % timestr
        time.sleep(3600)
