# -*-coding: utf-8 -*-
import numpy as np
from scipy.sparse import csr_matrix, coo_matrix
import scipy.sparse
import scipy.stats
import random
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt


def motif_times(adjacency_matrix, a):
    len_matrix = adjacency_matrix.shape[0]
    for i in range(a):
        print 'echo for motif is %d' % i
        adjacency_tran = np.transpose(adjacency_matrix)
        B_matrix_spare = adjacency_matrix.multiply(adjacency_tran)
        # B_full = np.ones((len_matrix, len_matrix))
        # B_full = csr_matrix(B_full, dtype=np.float64)
        # B_binary = binary(B_matrix_spare)
        # B_not = B_full - B_binary
        U_matrix = adjacency_matrix - B_matrix_spare
        # U_matrix = np.abs(U_matrix)
        U_tran = np.transpose(U_matrix)
        result_1 = U_matrix.dot(B_matrix_spare)
        result_1 = result_1.multiply(U_matrix)
        result_2 = B_matrix_spare.dot(U_tran)
        result_2 = result_2.multiply(U_tran)
        result_3 = U_tran.dot(U_matrix)
        result_3 = result_3.multiply(B_matrix_spare)
        adjacency_matrix = result_1 + result_2
        adjacency_matrix = adjacency_matrix + result_3
        # adjacency_matrix = result_1
        adjacency_tran = np.transpose(adjacency_matrix)
        adjacency_matrix = adjacency_matrix + adjacency_tran
        # print adjacency_matrix.nnz
        if len(adjacency_matrix.data) > 0:
            print np.max(adjacency_matrix.data), adjacency_matrix.nnz
    return adjacency_matrix


def construct_motif(txt_name, times):
    entry = []
    f = open(txt_name)
    while True:
        line = f.readline()
        if line:
            temp = []
            line = line.replace('\n', '')
            line = line.split(';')
            for i in range(len(line)):
                temp.append(int(line[i]))
            entry.append(temp)
        else:
            break
    spare_array_row = []
    spare_array_col = []
    spare_array_data = []
    entry_all = []
    for i in range(len(entry)):
        spare_array_row.append(entry[i][0])
        spare_array_col.append(entry[i][1])
        # spare_array_data.append(entry[i][2])
        spare_array_data.append(1)
        entry_all.append(entry[i][0])
        entry_all.append(entry[i][1])
    entry_unique = np.unique(entry_all)
    # newspare_array_row = []
    # newspare_array_col = []
    # counttt = 0
    # for nnn in range(len(spare_array_row)):
    #    if counttt % 300000 == 0:
    #        print 'echo is %d' % counttt
    #    counttt += 1
    #    id1 = spare_array_row[nnn]
    #    id2 = spare_array_col[nnn]
    #    id1new = np.where(entry_unique == id1)[0][0]
    #    id2new = np.where(entry_unique == id2)[0][0]
    #    newspare_array_row.append(id1new)
    #    newspare_array_col.append(id2new)
    maxnum = len(entry_unique)
    newspare_array_row = np.load('newspare_array_row.npy')
    newspare_array_col = np.load('newspare_array_col.npy')
    spare_array_data = np.load('spare_array_data.npy')
    # np.save('newspare_array_row.npy', newspare_array_row)
    # np.save('newspare_array_col.npy', newspare_array_col)
    # np.save('spare_array_data.npy', spare_array_data)
    adjacency_matrix = csr_matrix((spare_array_data, (newspare_array_row, newspare_array_col)), shape=(maxnum, maxnum), dtype = np.float64)
    data_array = adjacency_matrix.data
    lennn = data_array.shape[0]
    print lennn
    adjacency_matrix.data = np.ones((1, lennn), dtype=np.float64)[0]
    print adjacency_matrix.nnz
    result_B = adjacency_matrix.copy()
    result_C = motif_times(adjacency_matrix, times)
    print maxnum
    return result_C, entry_unique, result_B, maxnum


def binary(a_original):
    a = a_original.copy()
    for number in range(0, np.size(a, 0)):
        if number % 10000 == 0:
            print "echo is %d" % number
        for number_col in a.indices[a.indptr[number]:a.indptr[number+1]]:
            a[number, number_col] = 1
    return a


def compute_degree(a, maxnum):
    a = a.tocsr()
    print type(a)
    M_dict = {}
    for number in range(maxnum):
        count_degree = 0
        for number_col in a.indices[a.indptr[number]:a.indptr[number + 1]]:
            count_degree += 1
        M_dict[number] = count_degree
    return M_dict


def compute_degree_direct(a, maxnum, M_dict):
    b = a.tocsc()
    print type(b)
    N_dict = {}
    for number in range(maxnum):
        count_degree = 0
        for number_row in b.indices[b.indptr[number]:b.indptr[number + 1]]:
            if number_row == number:
                continue
            count_degree += 1
        N_dict[number] = count_degree
        N_dict[number] += int(M_dict[number])
    return N_dict


def top100(txt_name):
    f = open(txt_name)
    name_set = {}
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
            name_set[name_author] = int(id)
            count += 1
        else:
            break
    return name_set


def top(txt_name):
    f = open(txt_name)
    name_set = []
    count = 0
    while True:
        line = f.readline()
        if count >= 100:
            break
        if line:
            line = line.strip()
            line = line.split(';')
            name_author = line[1]
            name_set.append(name_author)
            count += 1
        else:
            break
    return name_set


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
    return entry


def construct_dict(txt_name):
    dict = {}
    f = open(txt_name)
    count = 0
    while True:
        line = f.readline()
        if line:
            count = count + 1
            line = line.strip()
            line = line.split(';')
            dict[int(line[1])] = line[0]
        else:
            break
    return dict

if __name__ == '__main__':
    result_C, entry_unique, result_B, maxnum = construct_motif('citation_network.txt', 1)
    #txt_name_pagerank='result/directed/result_direct_pagerank.txt'
    # txt_name1 = 'result/directed/result_direct_motifM7.txt'
    # txt_name2 = 'M7_result.txt'
    dict_h = h_index('h_index_all.txt')
    dict_id = construct_dict('author_domain_id.txt')
    count_number = 0
    N_author = {}
    M_author = {}
    H_array = []
    phi_array = []
    M_dict = compute_degree(result_C, maxnum)
    temp_dict = compute_degree(result_B, maxnum)
    N_dict = compute_degree_direct(result_B, maxnum, temp_dict)
    #data_array = []
    #for mm in range(300):
    #    temp_data = random.randint(0, maxnum - 1)
    #    while (temp_data in data_array):
    #        temp_data = random.randint(0, maxnum - 1)
    #    data_array.append(temp_data)
    #dict_hhvalue = sorted(dict_h.items(), key=lambda item: int(item[1]), reverse=True)
    #for i in range(1000):
    #    name = dict_hhvalue[i][0]
    #    data_array.append(name)
    #print len(data_array)
    for number in range(maxnum):
        if number % 3000 == 0:
            print 'echo is %d' % number
        #author_index = data_array[number]
        author_index = number
        count_N = N_dict[author_index]
        id = entry_unique[author_index]
        name = dict_id[id]
        hh_value = int(dict_h[name])
        if hh_value > 60:
            continue
        # if not(name in data_array):
        #    continue
        if count_N < 60:
            continue
        count_M = M_dict[author_index]
        phi = np.float(count_M * 1.0 / count_N)
        H_array.append(hh_value)
        N_author[name] = count_N
        M_author[name] = count_M
        count_number += 1
        phi_array.append(phi)
        if number < 10:
            print phi, hh_value, count_M, count_N
    print len(phi_array)
    print len(H_array)
    matrix_final = []
    matrix_final.append(H_array)
    matrix_final.append(phi_array)
    # np.save('result/npy/M5_low.npy', H_array)
    # np.save('result/npy/M5_low_Phi.npy', phi_array)
    print np.corrcoef(matrix_final)
    r_value, p_value = scipy.stats.pearsonr(phi_array, H_array)
    print r_value
    print p_value
    #plt.scatter(phi_array, H_array)
    #plt.show()
    #plt.savefig("result.png", format='png')


