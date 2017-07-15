import numpy as np


def read_co_author(txt_name):
    entry = []
    f = open(txt_name)
    count = 0
    while True:
        print "echo is %d" % count
        co_author = []
        line = f.readline()
        if line:
            line = line.replace('\n', '')
            line = line.split(' ')
            auther = line[1]
        else:
            break
        while True:
            line = f.readline()
            if line:
                if line == '\n':
                    entry.append([])
                    entry[count].append(auther)
                    entry[count].append(co_author)
                    count = count + 1
                    break
                line = line.replace('\n', '')
                if line[1] == '%':
                    line = line.split(' ')
                    co_author.append(line[1])
            else:
                break
    return entry


if __name__ == '__main__':
    entry = read_co_author('/home/xiaogang_xu/database/DBLP-2015/original-data/AMiner-Paper.txt')
    # print entry
    output = open('citations.txt', 'w')
    for number in range(len(entry)):
        author = entry[number][0]
        co_author = entry[number][1]
        for number_other in range(len(co_author)):
            a = "%s %s\n" % (author, co_author[number_other])
            output.write(a)
    output.close()
