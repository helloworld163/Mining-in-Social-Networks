import numpy as np


def read_h_index(txt_name):
    dict = {}
    f = open(txt_name)
    while True:
        line = f.readline()
        if line:
            line = line.strip()
            line = line.split(';')
            if dict.get(line[0]):
                continue
            else:
                dict[line[0]] = [line[1], line[2]]
        else:
            break
    f.close()
    return dict

def read(txt_name, dict):
    count = 0
    entry = []
    f = open(txt_name)
    while True:
        if count >= 50:
            break
        line = f.readline()
        if line:
            count = count + 1
            line = line.strip()
            line = line.split(';')
            if dict.get(line[1]):
                continue
            else:
                entry.append(line[1])
        else:
            break
    return entry


def co_author_number(txt_name):
    dict_number = {}
    f = open(txt_name)
    count = 0
    while True:
        line = f.readline()
        if line:
            count = count + 1
            line = line.strip()
            line = line.split(';')
            if dict_number.get(line[0]):
                continue
            else:
                dict_number[line[0]] = line[1]
        else:
            break
    return dict_number


if __name__ == '__main__':
    # dict = read_h_index('result_rank/h-index.txt')
    count = 0
    sum_h_index = 0
    sum_citation = 0
    sum_author = 0
    dict_number = co_author_number('co_author_number.txt')
    f = open('result_rank/result_pagerank.txt')
    while True:
        if count >= 30000:
            break
        line = f.readline()
        if line:
            count = count + 1
            line = line.strip()
            line = line.split(';')
            name = line[1]
            # list_of_score = dict[name]
            # sum_h_index = sum_h_index + int(list_of_score[0])
            # sum_citation = sum_citation + int(list_of_score[1])
            sum_author = sum_author + int(dict_number[name])
        else:
            break
    f.close()
    # print 'the mean of h-index is %d' % (sum_h_index/50)
    # print 'the mean of citation is %d' % (sum_citation / 50)
    print 'the mean of co-author is %d' % (sum_author / 30000)
    # entry_other = read('result_rank/result_motif_3.txt', dict)
    # output = open('result_rank/h-index.txt', 'a')
    # for i in range(len(entry_other)):
    #    a = "%s;\n" % (entry_other[i])
    #    output.write(a)
    # output.close()




