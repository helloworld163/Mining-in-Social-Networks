import numpy as np

def read_data(txt_name):
    f = open(txt_name)
    entry = {}
    count = 0
    count_inter = 0
    while True:
        if count >= 100:
            break
        line = f.readline()
        if line == '\n':
            entry[name] = interest
            count += 1
            count_inter = 0
            continue
        if line:
            line = line.strip()
            if count_inter % 2 == 0:
                name = line
                count_inter += 1
            if count_inter % 2 == 1:
                interest = line
        else:
            break
    return entry


if __name__ == '__main__':
    txt_name = 'data/task2/training.txt'
    entry = read_data(txt_name)
    for name in entry.keys():
        print name
        print entry[name]
