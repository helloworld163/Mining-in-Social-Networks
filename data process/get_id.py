import numpy as np


def construct(txt_name):
    print "construct begin:"
    entry = {}
    f = open(txt_name)
    count = 0
    author_id = 0
    while True:
        if count % 10000 == 0:
            print "echo for construct is %d" % count
        line = f.readline()
        if line:
            count = count + 1
            line = line.strip()
            line_name = line.split(';')
            author = line_name[0]
            if not(entry.get(author)):
                entry[author] = author_id
                author_id = author_id + 1
        else:
            break
    return entry, author_id


def trans_name_to_id(txt_name, entry, author_id):
    print "trans begin:"
    entry_id = []
    f = open(txt_name)
    count = 0
    while True:
        if count % 10000 == 0:
            print "echo for transform is %d" % count
        line = f.readline()
        if line:
            count = count + 1
            line = line.strip()
            line_name = line.split(';')
            author1 = line_name[0]
            author2 = line_name[1]
            if entry.get(author1) and entry.get(author2):
                id1 = entry[author1]
                id2 = entry[author2]
                entry_id.append([id1, id2])
            else:
                if entry.get(author1):
                    entry[author2] = author_id
                    id1 = entry[author1]
                    entry_id.append([id1, author_id])
                    author_id = author_id + 1
                elif entry.get(author2):
                    id2 = entry[author2]
                    entry[author1] = author_id
                    entry_id.append([author_id, id2])
                    author_id = author_id + 1
                else:
                    entry[author1] = author_id
                    id1 = author_id
                    author_id = author_id + 1
                    entry[author2] = author_id
                    id2 = author_id
                    author_id = author_id + 1
                    entry_id.append([id1, id2])
        else:
            break
    return entry_id, entry


if __name__ == '__main__':
    entry, author_id = construct('data/author_citation_domain.txt')
    entry_id, entry = trans_name_to_id('data/co_author_domain.txt', entry, author_id)
    output = open('data/co_author_domain_id.txt', 'w')
    for number in range(len(entry_id)):
        author = entry_id[number][0]
        co_author = entry_id[number][1]
        a = "%s %s\n" % (author, co_author)
        output.write(a)
    output.close()
    output = open('author_domain_id.txt', 'w')
    result = sorted(entry.items(), key=lambda item: item[1], reverse=False)
    for i in range(len(result)):
        a = "%s;%s\n" % (result[i][0], result[i][1])
        output.write(a)
    output.close()

