import numpy as np
import os

if __name__ == '__main__':
    source_dir = 'twitter/twitter/'
    file_search = []
    for root, sub_dirs, files in os.walk(source_dir):
        file_search = files
    name_set = []
    file_set = []
    for number in file_search:
        if number[len(number)-6: len(number)] == '.edges':
            name_file = number[0:len(number)-6]
            name_set.append(name_file)
            file_set.append(number)
    print len(file_set)
    print len(name_set)
    source_directort = 'twitter/twitter/'
    # txt_name = 'twitter/twitter/12831.edges'
    node_set = {}
    edge_set = {}
    for file_number in range(len(file_set)):
        if file_number % 100 == 0:
            print 'echo is %d' % file_number
        file_name = file_set[file_number]
        file_name = source_directort + file_name
        ff = open(file_name)
        while True:
            line = ff.readline()
            if line:
                line = line.strip()
                line = line.split(' ')
                for i in range(len(line)):
                    line[i] = int(line[i])
                edges_t = str(line[0]) + ';'
                edges_t = edges_t + str(line[1])
                if edge_set.get(edges_t):
                    edge_set[edges_t] += 1
                else:
                    edge_set[edges_t] = 1

                if node_set.get(str(line[0])):
                    node_set[str(line[0])] += 1
                else:
                    node_set[str(line[0])] = 1

                if node_set.get(str(line[1])):
                    node_set[str(line[1])] += 1
                else:
                    node_set[str(line[1])] = 1
            else:
                break
        ff.close()
    print len(edge_set.keys())
    print len(node_set.keys())
