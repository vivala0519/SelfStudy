import sys
import functools

def cmp(s1, s2):
    if len(s1) < len(s2):
        return -1
    elif len(s1) > len(s2):
        return 1
    else:
        if s1 < s2:
            return -1
        else:
            return 1

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    words = [sys.stdin.readline().rstrip() for i in range(N)]
    # print(words)
    words.sort(key=functools.cmp_to_key(cmp))
    # print(words)
    print(words[0])
    for i in range(1, len(words)):
        if words[i] == words[i-1]:
            pass
        else:
            print(words[i])