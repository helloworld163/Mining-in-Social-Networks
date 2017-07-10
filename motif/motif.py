import numpy as np
import string
from itertools import combinations, permutations


def compute_vol(Adjacency, node_pair):
    count = 0
    for i in range(len(node_pair)):
        node1 = node_pair[i][0]
        node2 = node_pair[i][1]
        if Adjacency[node1][node2] == 1 and Adjacency[node2][node1] == 1:
            for node_number in range(len(sigma)):
                if node_number == node1 or node_number == node2:
                    continue
                temp_node = sigma[node_number]
                if Adjacency[node1][temp_node] == 1 and Adjacency[node2][temp_node] == 1:
                    if (not(Adjacency[temp_node][node1])) and (not(Adjacency[temp_node][node2])):
                        count = count + 1

        elif Adjacency[node1][node2] == 1 and (not(Adjacency[node2][node1])) == 1:
            for node_number in range(len(sigma)):
                if node_number == node1 or node_number == node2:
                    continue
                temp_node = sigma[node_number]
                if Adjacency[node1][temp_node] and (not(Adjacency[node2][temp_node])):
                    if Adjacency[temp_node][node1] and Adjacency[temp_node][node2]:
                        count = count + 1
    count = int(count / 2)
    return count


def compute_cut(Adjacency, sigma, sigma_other):
    node_pair = list(permutations(sigma, 2))
    count1 = 0
    count2 = 0
    for number1 in range(len(node_pair)):
        node1 = node_pair[i][0]
        node2 = node_pair[i][1]
        for number2 in range(len(sigma_other)):
            node3 = sigma_other[number2]
            if Adjacency[node1][node2] == 1 and Adjacency[node2][node1] == 1:
                if Adjacency[node1][node3] == 1 and Adjacency[node2][node3] == 1:
                    if Adjacency[node3][node1] == 0 and Adjacency[node3][node2] == 0:
                        count1 = count1 + 1

            elif Adjacency[node1][node2] == 1 and Adjacency[node2][node1] == 0:
                if Adjacency[node1][node3] == 1 and Adjacency[node2][node3] == 0:
                    if Adjacency[node3][node1] == 1 and Adjacency[node3][node2] == 1:
                        count1 = count1 + 1

    node_pair_other = list(permutations(sigma_other, 2))
    for number3 in range(len(node_pair_other)):
        node1 = node_pair_other[i][0]
        node2 = node_pair_other[i][1]
        for number4 in range(len(sigma)):
            node3 = sigma[number4]
            if Adjacency[node1][node2] == 1 and Adjacency[node2][node1] == 1:
                if Adjacency[node1][node3] == 1 and Adjacency[node2][node3] == 1:
                    if Adjacency[node3][node1] == 0 and Adjacency[node3][node2] == 0:
                        count2 = count2 + 1

            elif Adjacency[node1][node2] == 1 and Adjacency[node2][node1] == 0:
                if Adjacency[node1][node3] == 1 and Adjacency[node2][node3] == 0:
                    if Adjacency[node3][node1] == 1 and Adjacency[node3][node2] == 1:
                        count2 = count2 + 1
    cutM = count1 + count2
    return cutM


def compute_conductance(Adjacency, sigma):
    print sigma
    sigma_other = []
    for i in range(len(Adjacency)):
        if i in sigma:
            continue
        sigma_other.append(i)
    [m, n] = Adjacency.shape
    print sigma_other
    node_pair = list(permutations(sigma, 2))
    vol_S = compute_vol(Adjacency, node_pair)

    node_pair_other = list(permutations(sigma, 2))
    vol_S_other = compute_vol(Adjacency, node_pair_other)

    cutM = compute_cut(Adjacency, sigma, sigma_other)
    print cutM, vol_S, vol_S_other
    conductance = cutM / (min(vol_S, vol_S_other))
    return conductance


if __name__ == '__main__':
    motif_matrix =[]
    # construct the motif adjacency matrix
    f = open('matrix.txt')
    while True:
        line = f.readline()
        if line:
            temp = []
            line = line.replace("\n", "")
            line = line.split(' ')
            for i in range(len(line)):
                temp.append(line[i])
            motif_matrix.append(temp)
        else:
            break
    for row in range(len(motif_matrix)):
        for col in range(len(motif_matrix[row])):
            motif_matrix[row][col] = int(motif_matrix[row][col])

    Adjacency = []
    fa = open('Adjacency.txt')
    while True:
        line = fa.readline()
        if line:
            temp = []
            line = line.replace("\n", "")
            line = line.split(' ')
            for i in range(len(line)):
                temp.append(line[i])
            Adjacency.append(temp)
        else:
            break
    for row in range(len(Adjacency)):
        for col in range(len(Adjacency[row])):
            Adjacency[row][col] = int(Adjacency[row][col])

    Adjacency = np.array(Adjacency)
    motif_matrix = np.array(motif_matrix)

    [m, n] = motif_matrix.shape
    # construct the degree matrix which has value only in the position of diagonal
    degree_matrix = np.zeros((m, n))
    for i in range(m):
        sum = 0
        for j in range(n):
            sum = sum + motif_matrix[i, j]
        degree_matrix[i][i] = sum
    # The laplace_matrix can be obtained by subtract from D and M
    D_2_1 = degree_matrix.copy()

    for i in range(m):
        for j in range(n):
            if D_2_1[i][j] != 0:
                D_2_1[i][j] = np.power(D_2_1[i][j], -0.5)

    Laplace_matrix = degree_matrix - motif_matrix
    Laplace_matrix = np.dot(D_2_1, Laplace_matrix)
    Laplace_matrix = np.dot(Laplace_matrix, D_2_1)
    # print Laplace_matrix
    eigen_value, eigen_vector = np.linalg.eig(Laplace_matrix)
    sort_eigen = np.argsort(eigen_value)
    sort_eigen = sort_eigen[-1::-1]
    lamda_two = eigen_vector[sort_eigen[1]]
    lamda_two = np.array(lamda_two)
    f = np.dot(D_2_1, lamda_two)

    sort_number = np.argsort(f)
    for sigma_number in range(len(sort_number)):
        if sigma_number != 0:
            continue
        sigma = []
        for i in range(5):
            sigma.append(sort_number[i])
        conductance = compute_conductance(Adjacency, sigma)
        print conductance
