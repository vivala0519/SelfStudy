
while True:
    try:
        # line = sys.stdin.readline().strip()
        s, t = input().split()

        idx = 0
        result = 0
        for i in range(len(t)):
            if t[i] == s[idx]:
                idx += 1
                if idx == len(s):
                    result = 1
                    break
        if result == 1:
            print('Yes')
        else:
            print('No')

    except:
        break
