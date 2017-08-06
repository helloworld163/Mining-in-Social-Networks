import numpy as np
import random


def read_motif(txt_name):
    entry = []
    f = open(txt_name)
    while True:
        line = f.readline()
        if line:
            temp = []
            line = line.replace('\n', '')
            line = line.split(';')
            for i in range(len(line)):
                temp.append(line[i])
            entry.append(temp)
        else:
            break
    for number in range(len(entry)):
        for number_entry in range(len(entry[number])):
            entry[number][number_entry] = int(entry[number][number_entry])
    spare_array_row = []
    spare_array_col = []
    spare_array_data = []
    spare_node = []
    entry_all = []
    count = 0
    for i in range(len(entry)):
        count += 1
        if not(entry[i][0] in spare_node) and (len(spare_node) < 100) and (entry[i][0] < 500):
            spare_node.append(entry[i][0])
        if not(entry[i][1] in spare_node) and (len(spare_node) < 100) and (entry[i][0] < 500):
            spare_node.append(entry[i][1])
        if len(spare_node) >= 100:
            break
    for i in range(len(entry)):
        if (entry[i][0] in spare_node) and (entry[i][1] in spare_node):
            spare_array_row.append(entry[i][0])
            spare_array_col.append(entry[i][1])
            spare_array_data.append(1)
            entry_all.append(entry[i][0])
            entry_all.append(entry[i][1])
        # spare_array_data.append(entry[i][2])
    entry_unique = np.unique(entry_all)
    spare_array_row = np.array(spare_array_row)
    spare_array_col = np.array(spare_array_col)
    np.save("array_row_direct.npy", spare_array_row)
    np.save("array_col_direct.npy", spare_array_col)
    np.save("unique_array_direct.npy", entry_unique)
    maxnum = len(entry_unique)
    Graph_basic_new = np.zeros((100, 100))
    for nn in range(len(spare_array_row)):
        id1 = spare_array_row[nn]
        id2 = spare_array_col[nn]
        id1new = np.where(entry_unique == id1)[0][0]
        id2new = np.where(entry_unique == id2)[0][0]
        Graph_basic_new[id1new][id2new] = 1
        # Graph_basic_new[id2new][id1new] = 1
    print maxnum
    return Graph_basic_new, entry_unique


def read_motif_undirect():
    spare_array_row = np.load("array_row.npy")
    spare_array_col = np.load("array_col.npy")
    entry_unique = np.load("unique_array.npy")
    maxnum = len(entry_unique)
    Graph_basic_new = np.zeros((100, 100))
    for nn in range(len(spare_array_row)):
        id1 = spare_array_row[nn]
        id2 = spare_array_col[nn]
        id1new = np.where(entry_unique == id1)[0][0]
        id2new = np.where(entry_unique == id2)[0][0]
        Graph_basic_new[id1new][id2new] = 1
        Graph_basic_new[id2new][id1new] = 1
    print maxnum
    return Graph_basic_new, entry_unique


def read_motif_direct():
    spare_array_row = np.load("array_row_direct.npy")
    spare_array_col = np.load("array_col_direct.npy")
    entry_unique = np.load("unique_array_direct.npy")
    maxnum = len(entry_unique)
    Graph_basic_new = np.zeros((100, 100))
    for nn in range(len(spare_array_row)):
        id1 = spare_array_row[nn]
        id2 = spare_array_col[nn]
        id1new = np.where(entry_unique == id1)[0][0]
        id2new = np.where(entry_unique == id2)[0][0]
        Graph_basic_new[id1new][id2new] = 1
    print maxnum
    return Graph_basic_new, entry_unique


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
    Graph_basic_new, entry_unique = read_motif('data/triple_r.txt')

