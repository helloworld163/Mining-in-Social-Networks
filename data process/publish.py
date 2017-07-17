import numpy as np


def compute_publish(txt_name):
    entry = {}
    f = open(txt_name)
    count = 0
    while True:
        if count % 10000 == 0:
            print "echo is %d" % count
        author_set = []
        line = f.readline()
        if not(line):
            break
        number_citation = 0
        while True:
            line = f.readline()
            line = unicode(line, "utf-8")
            if line:
                if line == '\n':
                    for number_author in range(len(author_set)):
                        if entry.get(author_set[number_author]):
                            entry[author_set[number_author]] = entry[author_set[number_author]] + number_citation
                        else:
                            entry[author_set[number_author]] = number_citation
                    count = count + 1
                    break
                line = line.replace('\n', '')
                if line[1] == '%':
                    number_citation = number_citation + 1
                if line[1] == '@':
                    line = line.replace('#', '')
                    line = line.replace('@', '')
                    line = line.strip()
                    line = line.split(',')
                    if len(line) > 0:
                        for i in range(len(line)):
                            if line[i] == '':
                                continue
                            if i == 0:
                                author_set.append(line[i])
                            else:
                                author_set.append(line[i][1:len(line[i])])
            else:
                break
    return entry


if __name__ == '__main__':
    entry = compute_publish('papers_by_domains.txt')
    result = sorted(entry.items(), key=lambda item: item[1], reverse=True)
    output = open('author_citation_domain.txt', 'w')
    # for number in entry_citation.keys():
    #     author = number
    for i in range(len(result)):
        a = "%s;%s\n" % (result[i][0].encode('utf-8'), result[i][1])
        output.write(a)
    output.close()