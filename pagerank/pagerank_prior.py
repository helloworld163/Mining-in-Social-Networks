# -*-coding: utf-8 -*-
import numpy as np

def graphMove(a):
    # 构造转移矩阵, we will construct the transfer matrix
    b = np.transpose(a)  # b为a的转置矩阵
    c = np.zeros((a.shape), dtype=float)
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            c[i][j] = a[i][j] / (b[j].sum())
    return c


def pagerank_value(P, vi, n, i_index):
    vi_vector = np.zeros((n, 1))
    vi_vector[i_index] = vi
    result = np.dot(P, vi_vector)
    sum = 0
    for number in range(len(result)):
        sum = sum + result[number]
    sum = float(sum)
    return sum


if __name__ == '__main__':
    a = np.array([[0, 1, 1, 0],
                  [1, 0, 0, 1],
                  [1, 0, 0, 1],
                  [1, 1, 0, 0]], dtype=float)
    # adjacency matrix

    c = graphMove(a)
    [m, n] = c.shape
    lamda = 0.6
    alpha = np.ones((m, 1))
    v = np.ones((m, 1))
    I = np.diag([1 for i in range(m)])
    I = np.array(I)
    c_transpose = np.transpose(c)
    P = np.array((I + lamda * I - c_transpose))
    P = np.linalg.inv(P)
    print P
    for i in range(m):
        alpha[i] = lamda * P[i][i] / m
        v[i] = alpha[i] / P[i][i]
    print alpha
    pagerank_score = []
    for number in range(m):
        score = pagerank_value(P, v[number], m, number)
        pagerank_score.append(score)
    print pagerank_score
