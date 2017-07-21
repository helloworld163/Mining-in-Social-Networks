import networkx as nx
import numpy as np


def construct_network(txt_name):
    # G = nx.Graph()
    G = nx.DiGraph()
    f = open(txt_name)
    count = 0
    while True:
        if count % 100000 == 0:
            print 'echo for construct network is%d' % count
        line = f.readline()
        if line:
            count = count + 1
            line = line.strip()
            author = line.split(';')
            node1 = int(author[0])
            node2 = int(author[1])
            G.add_node(node1)
            G.add_node(node2)
            G.add_edge(node1, node2)
        else:
            break
    return G


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
                entry[line[0]] = line[1]
        else:
            break
    print 'the length is %d' % (len(entry.keys()))
    return entry


def compute_average_h(txt_name, dict, entryd, dict_h):
    f = open(txt_name)
    count = 0
    entry = {}
    sum_co = 0
    author_all = []
    while True:
        if count >= 100:
            break
        # print 'echo is %d' % count
        line = f.readline()
        if line:
            line = line.strip()
            line = line.split(';')
            name = line[1]
            author_set = entryd[name]
            sum_temp = 0
            # h_my = dict_h[name]
            count = count + 1
            for i in range(len(author_set)):
                id = author_set[i]
                author_name = dict[id]
                h = dict_h[author_name]
                sum_temp += int(h)
            entry[name] = sum_temp * 1.0 / (len(author_set))
            author_all = author_all + author_set
        else:
            break
    author_all = np.array(author_all)
    author_unique = np.unique(author_all)
    for i in range(len(author_unique)):
        id = author_unique[i]
        author_name = dict[id]
        h = dict_h[author_name]
        sum_co = sum_co + int(h)
    # entry[name] = sum_temp * 1.0 / (len(author_set))
    # sum_co += sum_temp * 1.0 / (len(author_set))
    print 'the average of h-index for author is %lf' % (sum_co * 1.0 / len(author_unique))
    return entry


if __name__ == '__main__':
    G = construct_network('data/citation_network.txt')
    dict = construct_dict('author_domain_id.txt')
    entry = hop_co_author('result_rank/result_direct_pagerank.txt', G)
    dict_h = h_index('h_index_all.txt')

    entry_h = compute_average_h('result_rank/result_direct_pagerank.txt', dict, entry, dict_h)
    # print entry_h['Jian Pei']
    # print entry_h['Jie Tang']
    # print entry_h['Jun Yan']
    # print entry_h['Hanghang Tong']
    # print entry_h['Guoliang Li']
    # print entry_h['Wei Fan']

    # output = open('data/h_index_all.txt', 'w')
    # count = 0
    # dict = sorted(dict_h.items(), key=lambda item: int(item[1]), reverse=True)
    # for i in range(len(dict)):
    #    name = dict[i][0]
    #    number_of_co = dict[i][1]
    #    a = "%s;%d\n" % (name, int(number_of_co))
    #    output.write(a)
    # output.close()

