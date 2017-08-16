import numpy as np
import csv

def csv_read(csv_name):
    csv_reader = csv.reader(open(csv_name))
    count = 0
    citation = {}
    for row in csv_reader:
        if count == 0:
            count += 1
            continue
        # if count >= 100:
        #    break
        if citation.get(row[0]):
            continue
        citation[row[0]] = int(row[1])
        count += 1
    return citation


if __name__ == '__main__':
    csv_name = 'data/task3/train.csv'
    citation = csv_read(csv_name)
    txt_name_write = 'author_citation.txt'
    output = open(txt_name_write, 'w')
    dict = sorted(citation.items(), key=lambda item: int(item[1]), reverse=True)
    for i in range(len(dict)):
        name = dict[i][0]
        citation_number = dict[i][1]
        a = "%s;%d\n" % (name, int(citation_number))
        output.write(a)
    output.close()

