import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


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


def plot_map(txt_name, entry):
    f = open(txt_name)
    count = 0
    x = []
    y = []
    while True:
        if count >= 100:
            break
        print 'echo is %d' % count
        line = f.readline()
        if line:
            count = count + 1
            line = line.strip()
            line = line.split(';')
            h = entry[line[1]]
            x.append(count)
            y.append(h)
        else:
            break
    plt.figure()
    plt.plot(x, y)
    plt.show()


if __name__ == '__main__':
    # txt_name1 = 'h_index_all.txt'
    # txt_name2 = 'result_rank/result_motif_3.txt'
    # entry = h_index(txt_name1)
    # plot_map(txt_name2, entry)
    txt_name = 'result_motif_matrix2.txt'
    entry_number = {}
    f = open(txt_name)
    count = 0
    while True:
        line = f.readline()
        if line:
            count = count + 1
            line = line.strip()
            line = line.split(';')
            if len(line) != 2:
                continue
            if not (entry_number.get(line[0])):
                entry_number[line[0]] = int(line[1])
        else:
            break
    output = open('result_motif_test.txt', 'w')
    dict_h_name = sorted(entry_number.items(), key=lambda item: item[1], reverse=True)
    for number_name in range(len(dict_h_name)):
        name = dict_h_name[number_name][0]
        number = entry_number[name]
        a = "%s;%d;\n" % (name, number)
        output.write(a)
    output.close()


