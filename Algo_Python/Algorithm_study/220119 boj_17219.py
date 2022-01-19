import sys
first_line = sys.stdin.readline().rstrip()
input_site_num = first_line.split(' ')[0]
find_site_num = first_line.split(' ')[1]

input_arr = [sys.stdin.readline().rstrip() for i in range(int(input_site_num))]
dic = {}
for i in input_arr:
    dic[i.split(' ')[0]] = i.split(' ')[1]

find_arr = [sys.stdin.readline().rstrip() for i in range(int(find_site_num))]
for i in find_arr:
    print(dic[i])


fl = sys.stdin.readline().rstrip()
n, m = int(fl.split(' ')[0]), int(fl.split(' ')[1])
sites = [sys.stdin.readline().rstrip() for i in range(n)]
sites_dict = dict(i.split() for i in sites[:n])
find = [sys.stdin.readline().rstrip() for i in range(m)]
print('\n'.join(sites_dict.get(i) for i in find))
