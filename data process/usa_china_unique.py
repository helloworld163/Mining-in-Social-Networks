# -*-coding: utf-8 -*-
import numpy as np
import json
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


def construct_dict(txt_name):
    dict = {}
    f = open(txt_name)
    count = 0
    while True:
        line = f.readline()
        if line:
            count = count + 1
            line = line.strip()
            line = line.split(';')
            dict[line[0]] = int(line[1])
        else:
            break
    return dict


def h_index(txt_name):
    f = open(txt_name)
    count = 0
    entry = {}
    while True:
        line = f.readline()
        if line:
            count = count+1
            line = line.strip()
            line = line.split(';')
            if not(entry.get(line[0])):
                entry[line[0]] = int(line[1])
        else:
            break
    print 'the length is %d' % (len(entry.keys()))
    return entry


def rank_read(txt_name):
    f = open(txt_name)
    count = 0
    entry = {}
    while True:
        line = f.readline()
        if line:
            count = count + 1
            line = line.strip()
            line = line.split(';')
            if not (entry.get(line[1])):
                entry[line[1]] = count
        else:
            break
    return entry


if __name__ == '__main__':
    dict = construct_dict('author_domain_id.txt')
    # dict_h = h_index('h_index_all.txt')
    txt_name = 'department_real.txt'
    school_name_mit1 = 'Tsinghua'
    school_name_mit2 = '清华'
    school_name_stan1 = 'MSRA'
    school_name_stan2 = 'Microsoft Research Asia'
    school_name_cmu1 = 'Peking'
    school_name_cmu2 = '北京大学'
    school_name_ucb1 = 'zhejiang University'
    school_name_ucb2 = '浙江大学'
    name_depart = {}
    f = open(txt_name)
    while True:
        line = f.readline()
        if line:
            line = line.strip()
            line = line.split(';')
            name_depart[line[0]] = line[1]
        else:
            break
    school1 = []
    school2 = []
    school3 = []
    school4 = []
    for name in name_depart.keys():
        if (school_name_mit1 in name_depart[name]) or (school_name_mit2 in name_depart[name]):
            school1.append(name)
        elif (school_name_stan1 in name_depart[name]) or (school_name_stan2 in name_depart[name]):
            school2.append(name)
        elif (school_name_cmu1 in name_depart[name]) or (school_name_cmu2 in name_depart[name]):
            school3.append(name)
        elif (school_name_ucb1 in name_depart[name]) or (school_name_ucb2 in name_depart[name]):
            school4.append(name)
    print len(school1)
    print len(school2)
    print len(school3)
    print len(school4)
    txt_name2 = 'result_rank/result/binary/not-remove/result_binary_motif.txt'
    rank_entry = rank_read(txt_name2)
    rank_school = {}
    for i in range(len(school3)):
        if rank_entry.get(school3[i]):
            rank_school[school3[i]] = rank_entry[school3[i]]
    dict = sorted(rank_school.items(), key=lambda d:d[1], reverse=False)
    for i in range(5):
        print dict[i][0]


