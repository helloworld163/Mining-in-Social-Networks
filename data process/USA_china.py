import numpy as np
import json
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

if __name__ == '__main__':
    Source_dir = 'webwrong'
    file_search = []
    for Root, Sub_dirs, Files in os.walk(Source_dir):
        file_search = Files
    name_set = []
    file_set = []
    # txt_name = 'department_wrong.txt'
    # f = open(txt_name)
    # while True:
    #    line = f.readline()
    #    if line:
    #        line = line.strip()
    #        name_set.append(line)
    #        file_name = line + '.json'
    #        file_set.append(file_name)
    #    else:
    #        break
    for number in file_search:
        if number[len(number)-5: len(number)] == '.json':
            name_file = number[0:len(number)-5]
            name_set.append(name_file)
            file_set.append(number)
    source_directort = 'webwrong/'
    count = 0
    wrong_name = []
    output = open('department.txt', 'w')
    for file_number in range(len(file_set)):
        file_name = file_set[file_number]
        file_name = source_directort + file_name
        # file_name = 'result/Ari Frank.json'
        file_read = open(file_name, 'r')
        for line in file_read.readlines():
            file_dict = json.loads(line)
            result = file_dict['result']
            result = result[0]
            if not(result['aff'].get('desc')):
                wrong_name.append(name_set[file_number])
                break
            # department = result['aff']['desc_zh']
            department = result['aff']['desc']
            department = str(department).replace('\n', ' ')
            department = str(department).replace('\r', ' ')
            department = str(department).encode('utf-8')
            # print department
            count += 1
            a = "%s;%s\n" % (str(name_set[file_number]).encode('utf-8'), str(department).encode('utf-8'))
            output.write(a)
    output.close()
    print count
    output = open('department_wrong.txt', 'w')
    for number_s in range(len(wrong_name)):
        wname = wrong_name[number_s]
        a = "%s\n" % str(wname)
        output.write(a.encode('utf-8'))
    output.close()

