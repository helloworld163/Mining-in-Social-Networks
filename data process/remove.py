import numpy as np


def remove_repeat():
    entry = {}
    f = open('data/triple.txt')
    count = 0
    while True:
        if count % 1000 == 0:
            print 'echo is %d' % count
        line = f.readline()
        if line:
            line = line.replace('\n', '')
            line = line.split(';')
            # print line
            author = int(line[0])
            co_author = int(line[1])
            times_author = int(line[2])
            relation = '%d+%d' % (author, co_author)
            # relation = '+'.join(line)
            if not(entry.get(relation)):
                entry[relation] = times_author
            else:
                entry[relation] = max(entry[relation], times_author)
                #entry[relation] = entry[relation] + 1
            count = count + 1
        else:
            break
    return entry


if __name__ == '__main__':
    entry = remove_repeat()
    output = open('data/triple_r.txt', 'w')
    for str_number in entry.keys():
        str_key = str_number
        str_key = str_key.split('+')
        first = str_key[0]
        second = str_key[1]
        times = entry[str_number]
        a = "%s;%s;%d\n" % (first, second, times)
        output.write(a)
        # print first, second, times
    output.close()

