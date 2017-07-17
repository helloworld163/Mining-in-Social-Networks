import numpy as np


def construct_citation(txt_name):
    print "compute begin:"
    entry_citation = {}
    f = open(txt_name)
    count = 0
    while True:
        if count % 10000 == 0:
            print "echo is %d" % count
        line = f.readline()
        if line:
            line = line.strip()
            line = line.split(' ')
            if entry_citation.get(line[1]):
                entry_citation[line[1]] = entry_citation[line[1]] + 1
            else:
                entry_citation[line[1]] = 1
            count = count + 1
        else:
            break
    return entry_citation


if __name__ == '__main__':
    entry_citation = construct_citation('citations.txt')
    result = sorted(entry_citation.items(), key=lambda item: item[1], reverse=True)
    output = open('author_citation.txt', 'w')
    # for number in entry_citation.keys():
    #     author = number
    for i in range(len(result)):
        a = "%s %s\n" % (result[i][0], result[i][1])
        output.write(a)
    output.close()

