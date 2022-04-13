import sys

N = int(sys.stdin.readline().rstrip())
S = []
for _ in range(N):
    S += sys.stdin.readline().rstrip()
T = ''
start = 0
end = len(S) - 1
cnt = 0
while start <= end:
    if S[start] == S[end]:
        innerStart, innerEnd = start, end
        temp = False
        while innerStart <= innerEnd:
            if S[innerStart] < S[innerEnd]:
                T += S[start]
                start += 1
                temp = True
                break
            elif S[innerStart] > S[innerEnd]:
                T += S[end]
                end -= 1
                temp = True
                break
            else:
                innerStart += 1
                innerEnd -= 1
        if not temp:
            T += S[start]
            start += 1
    elif S[start] < S[end]:
        T += S[start]
        start += 1
    else:
        T += S[end]
        end -= 1
    cnt += 1
    if cnt % 80 == 0:
        T +='\n'
print(T)

