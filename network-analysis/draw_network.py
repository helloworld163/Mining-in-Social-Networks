import numpy as np
import networkx as nx
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt


def motif(Graph, a):
    Graph_new = np.array(Graph, dtype=np.float32)
    for number in range(a):
        print 'echo for motif is %d' % number
        B_matrix = Graph_new
        result_C = np.dot(B_matrix, B_matrix)
        result_C = np.multiply(B_matrix, result_C)
        Graph_new = result_C
        # row_sum = np.sum(Graph_new, 0)
        # for nn in range(5):
        #    row_sum[nn] = np.power(row_sum[nn], -0.5)
        # diag_sum = np.diag(row_sum)
        # print 'the diag matrix________________'
        # print diag_sum
        # temp = np.dot(diag_sum, Graph_new)
        # Graph_new = np.dot(temp, diag_sum)
        print 'the new matrix________________'
        print Graph_new
    return Graph_new


def construct(Graph):
    G = nx.Graph()
    for i in range(10):
        for j in range(10):
            if Graph[i][j] != 0:
                G.add_node(i)
                G.add_node(j)
                G.add_edge(i, j)
                G.add_edge(j, i)
    return G


if __name__ == '__main__':
    Graph_basic = [[0, 1, 1, 1, 1, 0, 0, 0, 0, 1],
                   [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                   [1, 0, 0, 1, 1, 1, 0, 1, 0, 0],
                   [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
                   [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                   [0, 0, 1, 0, 0, 0, 1, 1, 0, 0],
                   [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
                   [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
                   [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                   [1, 1, 0, 1, 0, 0, 0, 0, 0, 0]]
    random = nx.gnp_random_graph(10, 0.9)
    Graph_basic_new = np.zeros((10, 10))
    for number in range(len(random.edges())):
        node1 = random.edges()[number][0]
        node2 = random.edges()[number][1]
        Graph_basic_new[node1][node2] = 1
        Graph_basic_new[node2][node1] = 1
    print Graph_basic_new
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