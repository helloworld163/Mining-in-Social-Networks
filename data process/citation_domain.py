import numpy as np


def read_co_author(txt_name):
    entry = []
    f = open(txt_name)
    count = 0
    while True:
        if count % 10000 == 0:
            print "echo is %d" % count
        c_paper = []
        paper = []
        line = f.readline()
        if not(line):
            break
        while True:
            line = f.readline()
            if line:
                if line == '\n':
                    entry.append([])
                    entry[count].append(paper[0])
                    entry[count].append(c_paper)
                    count = count + 1
                    break
                line = line.replace('\n', '')
                if line[1] == 'i':
                    paper.append(line[6:len(line)])
                if line[1] == '%':
                    c_paper.append(line[2:len(line)])
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
            dict[line[0]] = int(line[1])
        else:
            break
    return dict


def paper_dict(txt_name):
    entry = {}
    count = 0
    f = open(txt_name)
    while True:
        if count % 10000 == 0:
            print "echo is %d" % count
        auther_set = []
        paper = []
        line = f.readline()
        if not (line):
            break
        while True:
            line = f.readline()
            if line:
                if line == '\n':
                    entry[paper[0]] = auther_set
                    count = count + 1
                    break
                line = line.replace('\n', '')
                if line[1] == 'i':
                    paper.append(line[6:len(line)])
                if line[1] == '@':
                    line_new = line[2:len(line)]
                    line_new = line_new.split(',')
                    for number in range(len(line_new)):
                        if number == 0:
                            auther_set.append(line_new[number])
                        else:
                            auther_set.append(line_new[number][1:len(line_new[number])])
                            # print line_new[number][1:len(line_new[number])]
            else:
                break
    print count
    return entry


def construct_network(txt_name, dict, paper_dict):
    network_result = []
    f = open(txt_name)
    count = 0
    while True:
        line = f.readline()
        if line:
            line = line.strip()
            line = line.split(';')
            author = line[0]
            citation_author = line[1]
            if paper_dict.get(author):
                author_set = paper_dict[author]
            else:
                continue
            if paper_dict.get(citation_author):
                citation_set = paper_dict[citation_author]
            else:
                continue
            for nn in range(len(author_set)):
                for mm in range(len(citation_set)):
                    id1 = dict[author_set[nn]]
                    id2 = dict[citation_set[mm]]
                    network_result.append([id1, id2])
            count += 1
        else:
            break
    print 'count is %d' % count
    return network_result


if __name__ == '__main__':
    dict = construct_dict('author_domain_id.txt')
    # entry = read_co_author('papers_by_domains.txt')
    paper_dict = paper_dict('papers_by_domains.txt')
    network_nn = construct_network('citations_domain.txt', dict, paper_dict)
    output = open('citation_network.txt', 'w')
    echo = 0
    for number_n in range(len(network_nn)):
        if echo % 10000 == 0:
            print 'echo is %d' % echo
        a = "%s;%s\n" % (str(network_nn[number_n][0]), str(network_nn[number_n][1]))
        echo += 1
        output.write(a)
    output.close()



