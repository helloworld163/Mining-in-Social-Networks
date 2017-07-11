# -*-coding: utf-8 -*-
import numpy as np

# def is_motif(matrix, node1, node2, node3):
#    if matrix[node1][node2] == 1:


def construct_motif(txt_name):
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
    # 首先从文本中得到有连接的点，以及其权重(这里指的是其共同出版的publish的数目)
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
    entry_unique = np.unique(entry_all)
    # 首先需要找出其中出现的author的数目，并且建立一个Unique的矩阵进行对应
    maxnum = len(entry_unique)
    del entry1
    del entry2
    # 按照之前所得的来构建我们需要的邻接矩阵
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
    # 按照不同的motif来计算最后的motif_matrix
    adjacency_matrix = np.transpose(adjacency_matrix)
    adjacency = np.transpose(adjacency_matrix)
    B_matrix = np.multiply(adjacency_matrix, adjacency)
    # U_matrix = adjacency_matrix - B_matrix
    result_C = np.dot(B_matrix, B_matrix)
    result_C = np.multiply(result_C, B_matrix)
    print maxnum
    return result_C, entry_unique

