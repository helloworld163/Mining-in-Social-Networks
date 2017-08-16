import numpy as np
import csv


def read_paper(txt_name):
    f = open(txt_name)
    entry = {}
    paper_time_dict = {}
    count = 0
    while True:
        line = f.readline()
        if line == '\n':
            author_set = author_set.split(',')
            entry[paper_index] = author_set
            paper_time_dict[paper_index] = paper_time
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
            # if line[0:2] == '#%':
        else:
            break
    return entry, paper_time_dict


def csv_read(csv_name):
    csv_reader = csv.reader(open(csv_name))
    count = 0
    citation = {}
    for row in csv_reader:
        if count == 0:
            count += 1
            continue
        if count >= 100:
            break
        citation[row[0]] = int(row[1])
        count += 1
    return citation


def author_to_paper(paper_entry):
    author_dic = {}
    for paper_name in paper_entry.keys():
        author_set = paper_entry[paper_name]
        for i in range(len(author_set)):
            if author_dic.get(author_set[i]):
                author_dic[author_set[i]].append(paper_name)
            else:
                author_dic[author_set[i]] = [paper_name]
    return author_dic


def co_author_compute(entry):
    co_author_dic = {}
    for paper_name in entry.keys():
        author_set = entry[paper_name]
        for i in range(len(author_set)):
            if co_author_dic.get(author_set[i]):
                for j in range(len(author_set)):
                    if author_set[j] == author_set[i]:
                        continue
                    elif author_set[j] in co_author_dic[author_set[i]]:
                        continue
                    else:
                        co_author_dic[author_set[i]].append(author_set[j])
            else:
                co_author_dic[author_set[i]] = []
                for j in range(len(author_set)):
                    if author_set[j] == author_set[i]:
                        continue
                    elif author_set[j] in co_author_dic[author_set[i]]:
                        continue
                    else:
                        co_author_dic[author_set[i]].append(author_set[j])
    return co_author_dic


def compute_publish(paper_entry, time_entry):
    people = {}
    for paper in paper_entry.keys():
        author_set = paper_entry[paper]
        time = time_entry[paper]
        for i in range(len(author_set)):
            if people.get(author_set[i]):
                if people[author_set[i]].get(time):
                    people[author_set[i]][time] += 1
                else:
                    people[author_set[i]][time] = 1
            else:
                people[author_set[i]] = {}
                people[author_set[i]][time] = 1
    return people


if __name__ == '__main__':
    txt_name = 'data/task3/papers.txt'
    entry, paper_time = read_paper(txt_name)
    # print entry
    author_paper = author_to_paper(entry)
    # print author_paper
    co_author = co_author_compute(entry)
    # print co_author
    csv_name = 'data/task3/train.csv'
    txt_name_write = 'co_author.txt'
    output = open(txt_name_write, 'w')
    for name in co_author.keys():
        author_set = co_author[name]
        for i in range(len(author_set)):
            a = "%s;%s\n" % (name, author_set[i])
            output.write(a)
    output.close()
    # citation = csv_read(csv_name)
    # for name in citation.keys():
    #    print name,
    #    print citation[name]
