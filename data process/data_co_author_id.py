import numpy as np


def construct_dir(txt_name):
    print "construct dir"
    entry = {}
    f = open(txt_name)
    count = 0
    while True:
        if count % 10000 == 0:
            print "echo for construct dir is %d" % count
        line = f.readline()
        if line:
            line = line.replace('\n', '')
            line_name = line.split(';')
            line_id = line.split(' ')
            name = line_name[1]
            id = line_id[0]
            # print name, id
            entry[name] = id
            count = count + 1
        else:
            break
    return entry


def trans_name_to_id(txt_name, entry):
    print "trans begin:"
    entry_id = []
    f = open(txt_name)
    count = 0
    succ = 0
    while True:
        if count % 10000 == 0:
            print "echo for transform is %d" % count
            print "succ = %d" % succ
        line = f.readline()
        if line:
            count = count + 1
            # line = line.replace('\n', '')
            line = line.strip()
            line_name = line.split(';')
            author1 = line_name[0]
            author2 = line_name[1]
            if entry.get(author1) and entry.get(author2):
                id1 = entry[author1]
                id2 = entry[author2]
            else:
                continue
            entry_id.append([id1, id2])
            succ = succ + 1
        else:
            break
    print "succ = %d" % succ
    return entry_id


if __name__ == '__main__':
    entry = construct_dir('author.txt')
    entry_id = trans_name_to_id('co_author_real.txt', entry)
    output = open('co_author_id.txt', 'w')
    print len(entry_id)
    for number in range(len(entry_id)):
        if len(entry_id[number]) != 2:
            continue
        author = entry_id[number][0]
        co_author = entry_id[number][1]
        a = "%s %s\n" % (author, co_author)
        output.write(a)
    output.close()

