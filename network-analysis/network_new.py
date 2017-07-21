import networkx as nx
import numpy as np
from itertools import combinations


def construct_network(txt_name):
    G = nx.Graph()
    f = open(txt_name)
    count = 0
    while True:
        if count % 1000 == 0:
            print 'echo for construct network is%d' % count
        line = f.readline()
        if line:
            count = count + 1
            line = line.strip()
            author = line.split(' ')
            node1 = int(author[0])
            node2 = int(author[1])
            G.add_node(node1)
            G.add_node(node2)
            G.add_edge(node1, node2)
            G.add_edge(node2, node1)
        else:
            break
    return G


def construct_adj(txt_name):
    edges = {}
    nodes = {}
    f = open(txt_name)
    count = 0
    while True:
        if count % 500000 == 0:
            print 'echo for construct network is%d' % count
        line = f.readline()
        if line:
            count = count + 1
            line = line.strip()
            author = line.split(' ')
            node1 = str(author[0])
            node2 = str(author[1])
            # result1 = ';'.join(node1 + node2)
            # result2 = ';'.join(node2 + node1)
            result1 = node1 + ';' + node2
            result2 = node2 + ';' + node1
            if not(edges.get(result1)):
                edges[result1] = 1
            else:
                edges[result1] += 1

            if not(edges.get(result2)):
                edges[result2] = 1
            else:
                edges[result2] += 1
            if not(nodes.get(int(node1))):
                nodes[int(node1)] = [int(node2)]
            else:
                if not(int(node2) in nodes[int(node1)]):
                    nodes[int(node1)].append(int(node2))

            if not(nodes.get(int(node2))):
                nodes[int(node2)] = [int(node1)]
            else:
                if not(int(node1) in nodes[int(node2)]):
                    nodes[int(node2)].append(int(node1))
            # edges.append([node1, node2])
            # edges.append([node2, node1])
        else:
            break
    return edges, nodes


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
            dict[line[0]] = int(line[1])
        else:
            break
    return dict

# def construct_h(txt_name):


def hop_co_author(txt_name, G):
    f = open(txt_name)
    count = 0
    entry = {}
    sum_co = 0
    while True:
        if count >= 100:
            break
        line = f.readline()
        if line:
            author_set_1 = []
            author_set_2 = []
            # author_set_3 = []
            count = count + 1
            line = line.strip()
            line = line.split(';')
            id = int(line[0])
            name = line[1]
            # result = nx.bfs_successors(G, id)
            result = nx.single_source_shortest_path_length(G, id)
            for distance in result.keys():
                if result[distance] == 1:
                    author_set_1.append(distance)
                elif result[distance] == 2:
                    author_set_2.append(distance)
                # elif result[distance] == 3:
                #    author_set_3.append(distance)
            # number_of_co = len(author_set_1) + len(author_set_2)
            # author_set = author_set_1 + author_set_2
            author_set = author_set_1
            # author_set = author_set + author_set_3
            # author_set = np.array(author_set)
            # author_set_unique = np.unique(author_set)
            # entry[name] = number_of_co
            entry[name] = author_set
            sum_co = sum_co + len(author_set)
        else:
            break
    print 'the average number of 2hop co-author is %d' % int(sum_co / 100)
    return entry


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
    print 'the length is %d' % (len(entry.keys()))
    return entry


def compute_average_h(G, nodes, author_name, dict, id):
    a = list(combinations(author_name, 2))
    echo = 0
    count = 0
    if nodes.get(int(id)):
        node_set = nodes[int(id)]
    else:
        node_set = []
    for number in range(len(a)):
        # if echo % 300000 == 0:
        #    print 'echo is %d' % echo
        echo += 1
        id1 = dict[a[number][0]]
        id2 = dict[a[number][1]]
        if not(nodes.get(int(id1))):
            continue
        if not(nodes.get(int(id2))):
            continue
        if not(int(id1) in nodes[int(id2)]):
            continue
        if not(int(id1) in node_set) or not(int(id2) in node_set):
            continue
        # id1 = dict[author_name[number]]
        node1 = str(id1)
        node2 = str(id2)
        id = str(id)
        result1 = node1 + ';' + node2
        result2 = node2 + ';' + node1
        result3 = node1 + ';' + id
        result4 = id + ';' + node1
        result5 = node2 + ';' + id
        result6 = id + ';' + node2
        # if G.get(result3) or G.get(result4):
        #    count += 1
        # if G.get(result5) or G.get(result6):
        #    count += 1
        if G.get(result1) or G.get(result2):
            if G.get(result3) or G.get(result4):
                if G.get(result5) or G.get(result6):
                    count += 1
    # print 'the average number of motif is %d' % (count)
    return count


def compute_average_h_s(G, nodes, author_name, dict, super):
    # a = list(combinations(author_name, 2))
    id = dict['Jian Pei']
    if nodes.get(int(id)):
        node_set = nodes[int(id)]
    else:
        node_set = []
    echo = 0
    count = 0
    for number in range(len(author_name)):
        if echo % 100 == 0:
            print 'echo is %d' % echo
        echo += 1
        # id1 = dict[a[number][0]]
        # id2 = dict[a[number][1]]
        id1 = dict[author_name[number]]
        if (int(id1) in node_set):
            count += super[int(id1)]
        #    continue
        # node1 = str(id1)
        # node2 = str(id2)
        # id = str(id)
        # result1 = node1 + ';' + node2
        # result2 = node2 + ';' + node1
        # result3 = node1 + ';' + id
        # result4 = id + ';' + node1
        # result5 = node2 + ';' + id
        # result6 = id + ';' + node2
        # if G.get(result3) or G.get(result4):
        #    count += super[int(node1)]
        # if G.get(result5) or G.get(result6):
        #    count += super[int(node2)]
        # if G.get(result1) or G.get(result2):
        #    if G.get(result3) or G.get(result4):
        #        if G.get(result5) or G.get(result6):
        #            count += 1
        #            count += super[int(node1)]
        #            count += super[int(node2)]
    print 'the average number of motif is %d' % (count)
    return count


if __name__ == '__main__':
    # G = construct_network('data/co_author_domain_id.txt')
    G, nodes = construct_adj('data/co_author_domain_id.txt')
    dict = construct_dict('author_domain_id.txt')
    # entry = hop_co_author('result_rank/result_motif.txt', G)
    dict_h = h_index('h_index_all.txt')
    dict_h_name = sorted(dict_h.items(), key=lambda item:item[1], reverse=True)
    author_name = []
    # super = {}
    # for i in range(1000):
    #    author_name.append(dict_h_name[i][0])

    # author_name1 = []
    for i in range(500):
        if i % 50 == 0:
            print 'the author is %d' % i
        author_name.append(dict_h_name[i][0])
        # id = dict[dict_h_name[i][0]]
        # count = compute_average_h(G, nodes, author_name, dict, id)
        # super[int(id)] = count
    # print author_name
    output = open('data/result_motif_matrix.txt', 'a+')
    echo = 0
    no_zero = 0
    for number_name in range(9754, len(dict_h_name), 1):
        echo += 1
        if echo % 500 == 0:
            print 'echo is %d' % echo
        name = dict_h_name[number_name][0]
        id = dict[name]
        count = compute_average_h(G, nodes, author_name, dict, id)
        if count != 0:
            no_zero += 1
        a = "%s;%d\n" % (name, count)
        output.write(a)
    print no_zero
    output.close()
