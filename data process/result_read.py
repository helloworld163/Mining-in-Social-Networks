import numpy

def read_name(txt_name):
    entry = []
    f = open(txt_name)
    while True:
        line = f.readline()
        if line:
            temp = []
            line = line.replace('\n', '')
            line = line.split(';')
            print line
            for i in range(len(line)):
                temp.append(line[i])
            entry.append(temp)
        else:
            break
    dict_name = {}
    for number in range(len(entry)):
        dict_name[entry[number][1]] = entry[number][0]
    return dict_name

if __name__ == '__main__':
    entry = []

    f = open('result3.txt')
    while True:
        line = f.readline()
        if line:
            temp = []
            line = line.replace('\n', '')
            line = line.split(' ')
            print line
            for i in range(len(line)):
                temp.append(line[i])
            entry.append(temp)
        else:
            break
    for number in range(len(entry)):
        entry[number][0] = float(entry[number][0])
    ranklist = {}
    for i in range(len(entry)):
        ranklist[entry[i][1]] = entry[i][0]
    dict = sorted(ranklist.items(), key=lambda item:item[1], reverse=True)
    top_k = []
    for i in range(50):
        top_k.append(dict[i][0])
    print top_k
    name_txt = 'author_domain_id.txt'
    dict_name = read_name(name_txt)
    output = open('result_motif3_100.txt', 'w')
    for i in range(100):
        a = "%s;%s;%lf\n" % (dict[i][0], dict_name[dict[i][0]], dict[i][1])
        output.write(a)
    output.close()
