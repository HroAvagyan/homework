import re


def extract_nums(s):
    my_lst = []
    with open(s) as file:
        for line in file:
            my_lst.append(re.findall(r'-?\d+',line))
    return my_lst



def sort_lines_by_avg(in_file, out_file=None):
    list_of_integers = extract_nums(in_file)
    lst = []
    for row in list_of_integers:
        ints = list(map(int,row))
        lst.append(sum(ints) // len(ints))

    with open('data.txt','r') as file:
        d = dict(zip(file.readlines(),lst))
        sorted_lines = sorted(d.keys(), key=lambda x: d[x],reverse=True)
        
    if out_file is None:
        out_file = in_file
    with open(out_file,'w') as result:
        result.writelines(sorted_lines)
        
sort_lines_by_avg('data.txt','result.txt')
