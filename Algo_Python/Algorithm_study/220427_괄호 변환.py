def divide(s):
    u = ''
    v = ''
    leftBracket = 0
    rightBracket = 0
    i = 0
    while True:
        if leftBracket == rightBracket:
            if leftBracket == 0 or rightBracket == 0:
                pass
            else:
                v += s[i:]
                break
        if s[i] == '(':
            leftBracket += 1
            u += '('
        else:
            rightBracket += 1
            u += ')'
        i += 1
    return u, v

def check(u):
    temp = []
    for i in u:
        if i == '(':
            temp.append(i)
        else:
            if temp:
                temp.pop()
    if not temp:
        return True
    else:
        return False

def solution(p):
    if not p:
        return ""

    u, v = divide(p)

    if check(u):
        return u + solution(v)
    else:
        result = '(' + solution(v) + ')'

        for p in u[1:len(u) - 1]:
            if p == '(':
                result += ')'
            else:
                result += '('
        return result

if __name__ == '__main__':
    p = '()))((()'
    solution(p)