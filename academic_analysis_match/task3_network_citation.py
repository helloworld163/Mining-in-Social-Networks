import numpy as np


def read_paper(txt_name):
    f = open(txt_name)
    entry = {}
    paper_citation = {}
    citation_paper = []
    count = 0
    while True:
        line = f.readline()
        if line == '\n':
            author_set = author_set.split(',')
            entry[paper_index] = author_set
            paper_citation[paper_index] = citation_paper
            citation_paper = []
            count += 1
            continue
        if line:
            line = line.strip()
            if line[0:6] == '#index':
                paper_index = line[6:len(line)]
            if line[0:2] == '#@':
                author_set = line[2:len(line)]
            if line[0:2] == '#t':
                paper_time = line[2:len(line)]
            if line[0:2] == '#%':
                citation_paper.append(line[2:len(line)])
        else:
            break
    return entry, paper_citation


def author_id(txt_name):
    f = open(txt_name)
    name_dic = {}
    count = 0
    while True:
        line = f.readline()
        if line:
            line = line.strip()
            line = line.split(';')
            name_author = line[0]
            id = int(line[1])
            if name_dic.get(name_author):
                continue
            else:
                name_dic[name_author] = id
            count += 1
        else:
            break
    return name_dic


if __name__ == '__main__':
    txt_name = 'data/task3/papers.txt'
    id_txt_name = 'author_id.txt'
    entry, paper_citation = read_paper(txt_name)
    # np.save('entry.npy', entry)
    # np.save('paper_citation.npy', paper_citation)
    name_dic = author_id(id_txt_name)
    txt_name_write = 'network_citation.txt'
    output = open(txt_name_write, 'w')
    for paper in paper_citation.keys():
        referenced = entry[paper]
        paper_set = paper_citation[paper]
        for i in range(len(paper_set)):
            reference = entry[paper_set[i]]
            if len(reference) == 0:
                continue
            for name1 in range(len(reference)):
                for name2 in range(len(referenced)):
                    id1 = name_dic[reference[name1]]
                    id2 = name_dic[referenced[name2]]
                    a = "%d;%d\n" % (id1, id2)
                    output.write(a)
    output.close()
