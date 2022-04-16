
v = ('a', 'i', 'y', 'e', 'o', 'u')
c = ('b', 'k', 'x', 'z', 'n', 'h', 'd', 'c', 'w', 'g', 'p', 'v', 'j', 'q', 't', 's', 'r', 'l', 'm', 'f')


while True:
    try:
        S = input()
        result = ''
        for i in range(len(S)):
            if S[i].lower() in v:
                if S[i].isupper():
                    k = S[i].lower()
                    for j in range(6):
                        if v[j] == k:
                            a = v[(j + 3) % 6]
                            result += a.upper()
                elif S[i].islower():
                    for j in range(6):
                        if v[j] == S[i]:
                            a = v[(j + 3) % 6]
                            result += a
            elif S[i].lower() in c:
                if S[i].isupper():
                    k = S[i].lower()
                    for j in range(20):
                        if c[j] == k:
                            a = c[(j + 10) % 20]
                            result += a.upper()
                elif S[i].islower():
                    for j in range(20):
                        if c[j] == S[i]:
                            a = c[(j + 10) % 20]
                            result += a
            else:
                result += S[i]

        print(result)
    except:
        break