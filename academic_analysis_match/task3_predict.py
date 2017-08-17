import numpy as np
import csv

def read_paper(txt_name):
    f = open(txt_name)
    entry = {}
    paper_citation = {}
    paper_time_dic = {}
    citation_paper = []
    count = 0
    while True:
        line = f.readline()
        if line == '\n':
            author_set = author_set.split(',')
            entry[paper_index] = author_set
            paper_citation[paper_index] = citation_paper
            paper_time_dic[paper_index] = paper_time
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
    return entry, paper_citation, paper_time_dic


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


def csv_read(csv_name):
    csv_reader = csv.reader(open(csv_name))
    count = 0
    citation = {}
    for row in csv_reader:
        if count == 0:
            count += 1
            continue
        citation[row[0]] = int(row[1])
        count += 1
    return citation


def compute_every_year(author_paper, paper_citation, paper_time):
    author_citation_dic = {}
    for paper in paper_citation.keys():
        author_set = author_paper[paper]
        time = paper_time[paper]
        citation_number = len(paper_citation[paper])
        for i in range(len(author_set)):
            if author_citation_dic.get(author_set[i]):
                if author_citation_dic[author_set[i]].get(time):
                    author_citation_dic[author_set[i]][time] += citation_number
                else:
                    author_citation_dic[author_set[i]][time] = citation_number
            else:
                author_citation_dic[author_set[i]] = {}
                author_citation_dic[author_set[i]][time] = citation_number
    return author_citation_dic


if __name__ == '__main__':
    id_txt_name = 'author_id.txt'
    csv_name = 'data/task3/train.csv'
    txt_paper = 'data/task3/papers.txt'
    entry, paper_citation, paper_time = read_paper(txt_paper)
    # name_dic = author_id(id_txt_name)
    # citation = csv_read(csv_name)
    author_citation_dic = compute_every_year(entry, paper_citation, paper_time)
    txt_name_write = 'citation_every_year.txt'
    output = open(txt_name_write, 'w')
    for number in author_citation_dic.keys():
        name = number
        dic = author_citation_dic[name]
        a = "%s(" % name
        output.write(a)
        for time in dic.keys():
            number = dic[time]
            a = "%s:%d;" % (time, int(number))
            output.write(a)
        a = ")\n"
        output.write(a)
    output.close()

