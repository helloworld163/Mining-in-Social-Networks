import numpy as np
import networkx as nx
import random
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt


def motif(Graph, a):
    Graph_new = np.array(Graph, dtype=np.float32)
    for number in range(a):
        print 'echo for motif is %d' % number
        Graph_new_tran = np.transpose(Graph_new)
        B_matrix = np.multiply(Graph_new, Graph_new_tran)
        U_matrix = Graph_new - B_matrix
        U_matrix_tran = np.transpose(U_matrix)
        result_1 = np.dot(U_matrix_tran, B_matrix)
        result_1 = np.multiply(result_1, U_matrix_tran)
        result_2 = np.dot(B_matrix, U_matrix)
        result_2 = np.multiply(result_2, U_matrix)
        result_3 = np.dot(U_matrix, U_matrix_tran)
        result_3 = np.multiply(result_3, B_matrix)
        result_4 = np.add(result_1, result_2)
        result_5 = np.add(result_4, result_3)
        Graph_new = result_5
        print 'the new matrix________________'
        print Graph_new
    return Graph_new


def construct(Graph):
    G = nx.DiGraph()
    for i in range(10):
        for j in range(10):
            if Graph[i][j] != 0:
                G.add_node(i)
                G.add_node(j)
                G.add_edge(i, j)
    return G


if __name__ == '__main__':
    Graph_basic = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                   [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [1, 1, 0, 0, 1, 1, 0, 0, 0, 0],
                   [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                   [1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    # random_map = nx.gnp_random_graph(10, 0.6)
    # Graph_basic_new = np.zeros((10, 10))
    # for number in range(len(random_map.edges())):
    #    id = random.randint(0, 1)
    #    node1 = random_map.edges()[number][id]
    #    node2 = random_map.edges()[number][1-id]
    #    Graph_basic_new[node1][node2] = 1
    # print Graph_basic_new
    limits = plt.axis('off')
    for aa in range(3):
        Graph = motif(Graph_basic, aa)
        G = construct(Graph)
        plt.subplot(1, 3, aa+1)
        position = nx.spring_layout(G)
        nodes = nx.draw_networkx_nodes(G, pos=position)
        edges = nx.draw_networkx_edges(G, pos=position)
        labels = nx.draw_networkx_labels(G, pos=position)
    plt.show()