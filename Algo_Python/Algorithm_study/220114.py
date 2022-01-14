import sys
if __name__ == '__main__':
    s = sys.stdin.readline().rstrip()
    print(s)
    zero, one = 0, 0
    temp = s[0]
    for i in range(1, len(s)):
        if s[i-1] != s[i]:
            temp += s[i]
    print(temp)
    arr = []
    for i in range(len(temp)):
        if temp[i] == '0':
            zero += 1
        else:
            one += 1
    arr.append(zero)
    arr.append(one)
    result = min(arr)
    print(result)