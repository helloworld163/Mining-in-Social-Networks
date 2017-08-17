from task3_data import co_author_compute, read_paper
import numpy as np


def read_data_interest(txt_name):
    f = open(txt_name)
    entry = {}
    count = 0
    count_inter = 0
    while True:
        line = f.readline()
        if line == '\n':
            entry[name] = interest
            count += 1
            count_inter = 0
            continue
        if line:
            line = line.strip()
            if count_inter % 2 == 0:
                name = line
                count_inter += 1
            if count_inter % 2 == 1:
                interest = line
                interest = interest.split(',')
        else:
            break
    return entry


def read_valid():
    txt_name = 'data/task2/validation.txt'
    valid_name = []
    f = open(txt_name)
    while True:
        line = f.readline()
        if line == '\n':
            continue
        if line:
            line = line.strip()
            name = line
            valid_name.append(name)
        else:
            break
    return valid_name


def valid_interest_compute(valid_name, co_author, entry_interest):
    name_to_interest = {}
    count_wrong = 0
    for name_number in range(len(valid_name)):
        name = valid_name[name_number]
        if name in entry_interest.keys():
            name_to_interest[name] = entry_interest[name]
        else:
            if co_author.get(name):
                co_author_set = co_author[name]
            else:
                name_to_interest[name] = []
                continue
            if len(co_author_set) == 0:
                name_to_interest[name] = []
                continue
            else:
                interest_this = []
                for i in range(len(co_author_set)):
                    if co_author_set[i] in entry_interest.keys():
                        interest_that = entry_interest[co_author_set[i]]
                        for j in range(len(interest_that)):
                            if interest_that[j] in interest_this:
                                continue
                            else:
                                interest_this.append(interest_that[j])
                    else:
                        continue
                name_to_interest[name] = interest_this
    print 'count wrong is %d' % count_wrong
    return name_to_interest


if __name__ == '__main__':
    txt_name = 'data/task2/training.txt'
    txt_name_paper = 'data/task3/papers.txt'
    entry, paper_time = read_paper(txt_name_paper)
    co_author = co_author_compute(entry)
    entry_interest = read_data_interest(txt_name)
    valid_name = read_valid()
    name_to_interest = valid_interest_compute(valid_name, co_author, entry_interest)
    count_zero = 0
    count_succ = 0
    for number in name_to_interest.keys():
        if len(name_to_interest[number]) == 0:
            count_zero += 1
        else:
            count_succ += 1
    print 'count zero is %d' % count_zero
    print 'count not zeros is %d' % count_succ
