import numpy as np


def read_matrix_from_txt(txt_name):
    entry = []
    f = open(txt_name)
    while True:
        line = f.readline()
        if line:
            temp = []
            line = line.replace('\r\n', '')
            line = line.split('	')
            for i in range(len(line)):
                temp.append(line[i])
            entry.append(temp)
        else:
            break
    for number in range(len(entry)):
        for number_entry in range(len(entry[number])):
            entry[number][number_entry] = int(entry[number][number_entry])

    entry1 = []
    entry2 = []
    entry_all = []
    for i in range(len(entry)):
        entry1.append(entry[i][0])
        entry_all.append(entry[i][0])
        entry2.append(entry[i][1])
        entry_all.append(entry[i][1])
    # maxnum1 = max(entry1)
    # maxnum2 = max(entry2)
    # print maxnum1
    # print maxnum2
    entry_unique = np.unique(entry_all)
    maxnum = len(entry_unique)
    del entry1
    del entry2
    adjacency_matrix = np.zeros((maxnum, maxnum))
    for i in range(len(entry)):
        node1 = entry[i][0]
        node2 = entry[i][1]
        weight = entry[i][2]
        node1_in_matrix = np.argwhere(entry_unique == node1)
        node2_in_matrix = np.argwhere(entry_unique == node2)
        # undirected link
        adjacency_matrix[node1_in_matrix[0][0]][node2_in_matrix[0][0]] = weight
        adjacency_matrix[node2_in_matrix[0][0]][node1_in_matrix[0][0]] = weight
    print maxnum
    return adjacency_matrix, entry_unique


if __name__ == '__main__':
    adjacency_matrix = read_matrix_from_txt('AA.txt')

