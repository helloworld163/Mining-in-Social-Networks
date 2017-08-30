# -*-coding: utf-8 -*-
import numpy as np
import networkx as nx
import random
# import matplotlib
# matplotlib.use('TkAgg')
# from matplotlib import pyplot as plt
from scipy.sparse import csr_matrix
from scipy.sparse import diags
MAX_TIME = 30000


# 这个函数是对用Numpy array的邻接矩阵进行归一化的函数
def graphMove(a):
    b = np.transpose(a)
    c = np.zeros((a.shape), dtype=float)
    for j in range(a.shape[1]):
        if b[j].sum() == 0:
            continue
        else:
            c[j] = b[j] / (b[j].sum())
    c = np.transpose(c)
    return c


# 这个函数是对用稀疏矩阵方式的邻接矩阵进行归一化的函数
def graphMove_newest(a):
    d = a.sum(0)
    d = np.array(d)
    d = d[0]
    # D_matrix在这里是要构造D^(-1/2)
    dd = map(lambda x: 0 if x==0 else np.power(x, -0.5), d)
    D_matrix =diags(dd, 0)
    C = D_matrix.dot(a)
    C = C.dot(D_matrix)
    a = C
    a = np.transpose(a)
    return a


#设置我们pagerank值的初始化
def firstPr(c):
    pr = np.zeros((c.shape[0], 1), dtype=float)
    for i in range(c.shape[0]):
        pr[i] = float(1) / c.shape[0]
    return pr


#进行pagerank迭代的函数，一共要迭代30000次
def pageRank(p, m, v):
    e = np.ones((m.shape[0], 1))
    n = m.shape[0]
    count = 0
    while count <= MAX_TIME:
        if count % 10000 == 0:
            print "echo is %d" % count
        v = p * m.dot(v) + ((1 - p) / n) * e
        count = count + 1
    return v


# 在numpy array的矩阵下，强行将其变为对称
def symmetry(matrix):
    len_matrix = matrix.shape[0]
    for i in range(len_matrix):
        matrix[:, i] = np.transpose(matrix[i])
    return matrix


# 在稀疏矩阵表示的矩阵下，强行将其变为对称
def symmetry_new(a):
    for number in range(0, np.size(a, 0)):
        for number_col in a.indices[a.indptr[number]:a.indptr[number+1]]:
            if number_col < number:
                a[number, number_col] = a[number_col, number]
            else:
                continue
    return a


# 构建numpy array方式的motif矩阵
def motif(Graph, a):
    # Graph_new = np.array(Graph, dtype=np.float32)
    Graph_new = Graph
    for number in range(a):
        if number % 50 == 0:
            print 'echo for motif is %d' % number
        Graph_new_tran = np.transpose(Graph_new)
        # 构建B
        B_matrix = Graph_new.multiply(Graph_new_tran)
        result_C = B_matrix.dot(B_matrix)
        result_C = result_C.multiply(B_matrix)
        Graph_new = result_C
        # 进行归一化，并且是每隔一轮进行一次
        if number % 2 == 0:
            row_sum = np.array(Graph_new.sum(0))[0]
            for nn in range(Graph_new.shape[0]):
                if row_sum[nn] == 0:
                    continue
                row_sum[nn] = np.power(row_sum[nn], -0.5)
            dim_m = Graph_new.shape[0]
            diag_sum = diags(row_sum, 0, shape=(dim_m, dim_m))
            temp = diag_sum.dot(Graph_new)
            Graph_new_n = temp.dot(diag_sum)
            # 将算得的矩阵强行对称
            Graph_new = symmetry_new(Graph_new_n)
        else:
            Graph_new = symmetry_new(Graph_new)
            # 将算得的矩阵强行对称
        # print 'the new matrix________________'
        # print Graph_new
    return Graph_new


# 构建稀疏矩阵方式表达的邻接矩阵的motif矩阵
def motif_arr(Graph, a):
    Graph_new = np.array(Graph, dtype=np.float32)
    for number in range(a):
        if number % 50 == 0:
            print 'echo for motif is %d' % number
        B_matrix = Graph_new
        result_C = np.dot(B_matrix, B_matrix)
        result_C = np.multiply(result_C, B_matrix)
        Graph_new = result_C
        if number % 2 == 0:
            row_sum = np.sum(Graph_new, 0)
            for nn in range(Graph_new.shape[0]):
                if row_sum[nn] == 0:
                    continue
                row_sum[nn] = np.power(row_sum[nn], -0.5)
            diag_sum = np.diag(row_sum)
            temp = np.dot(diag_sum, Graph_new)
            Graph_new = np.dot(temp, diag_sum)
        Graph_new = symmetry(Graph_new)
        # print 'the new matrix________________'
        # print Graph_new
    return Graph_new


if __name__ == '__main__':
    # 构建邻接矩阵的大小是1000 * 10000
    Graph_basic_new = np.zeros((1000, 1000))
    # spare_array_row = []
    # spare_array_col = []
    # spare_array_data = []
    # 大约生成6w条边
    for number in range(60000):
        node1 = random.randint(0, 999)
        node2 = random.randint(0, 999)
        # spare_array_row.append(node1)
        # spare_array_col.append(node2)
        # spare_array_data.append(1)
        Graph_basic_new[node1][node2] = 1
        Graph_basic_new[node2][node1] = 1
    maxnum = 1000
    # adjacency_matrix = csr_matrix((spare_array_data, (spare_array_row, spare_array_col)), shape=(maxnum, maxnum), dtype=np.float64)
    # print Graph_basic_new
    result = []
    # aa在这里就是表示motif的阶数
    for aa in range(500):
        Graph = motif_arr(Graph_basic_new, aa)
        print 'sum is %lf' % np.sum(Graph)
        # print adjacency_matrix.nnz
        # 获得了motif的邻接矩阵之后，先归一化，之后进行pagerank
        M = graphMove(Graph)
        pr = firstPr(M)
        p = 0.8
        v = pageRank(p, M, pr)
        v = v.reshape((1, v.shape[0]))[0]
        b = np.argsort(v)
        # 将排序的结果保存下来
        result.append(b)
    # 构建矩阵，其中每一列是上面每一个阶数下的pagerank的排序情况，便于最后输出到txt
    result_matrix = np.zeros((1000, len(result)))
    for number in range(len(result)):
        for k in range(1000):
            result_matrix[k][number] = result[number][k]
    # 将其输出
    output = open('result_ranl/exper/result_1000_new.txt', 'w')
    for i in range(1000):
        for j in range(len(result)):
            if j != len(result) - 1:
                a = "%d;" % (result_matrix[i][j])
                output.write(a)
            else:
                a = "%d" % (result_matrix[i][j])
                output.write(a)
        a = "\n"
        output.write(a)
    output.close()
