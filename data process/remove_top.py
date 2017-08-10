import numpy as np

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
                entry[line[0]] = line[1]
        else:
            break
    print 'the length is %d' % (len(entry.keys()))
    return entry

if __name__ == '__main__':
    dict_h = h_index('h_index_all.txt')
    txt_name1 = 'result_rank/directed/result_direct_motifM9.txt'
    txt_name2 = 'result_rank/directed/removed/result_direct_motifM9_remove_top100.txt'
    dict = sorted(dict_h.items(), key=lambda item: int(item[1]), reverse=True)
    name_set = []
    for i in range(100):
        name = dict[i][0]
        name_set.append(name)
    output = open(txt_name2, 'w')
    f = open(txt_name1)
    count = 0
    while True:
        line = f.readline()
        if count >= 100:
            break
        if line:
            line = line.strip()
            line = line.split(';')
            name_author = line[1]
            id = line[0]
            score = line[2]
            if name_author in name_set:
                continue
            else:
                count += 1
                a = "%s;%s;%s\n" % (id, name_author, score)
                output.write(a)
        else:
            break
    output.close()
