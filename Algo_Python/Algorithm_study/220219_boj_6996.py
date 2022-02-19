# a, b = 'bizarre', 'brazier'
import sys
n = int(sys.stdin.readline().rstrip())
result = []
for _ in range(n):
    a, b = map(str, sys.stdin.readline().rstrip().split())

    if len(a) != len(b):
        temp = a + ' & ' + b + ' are NOT anagrams.'
        result.append(temp)
    else:
        a_arr, b_arr = [], []

        for i in a:
            a_arr.append(i)
        for i in b:
            b_arr.append(i)
        a_arr.sort()
        b_arr.sort()

        i = 0
        while i < len(a_arr):
            if a_arr[i] != b_arr[i]:
                temp = a + ' & ' + b + ' are NOT anagrams.'
                result.append(temp)
                break
            i += 1
        if i == len(a_arr):
            temp = a + ' & ' + b + ' are anagrams.'
            result.append(temp)
for i in result:
    print(i)
