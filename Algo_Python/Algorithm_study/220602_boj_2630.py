import sys
N = int(sys.stdin.readline())

page = []
for _ in range(N):
    page.append(list(map(int, sys.stdin.readline().split())))

white = 0
blue = 0

def re(x, y, N):
    global white, blue
    temp = page[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if temp != page[i][j]:
                re(x, y, N // 2)
                re(x, y + N // 2, N // 2)
                re(x + N // 2, y, N // 2)
                re(x + N // 2, y + N // 2, N // 2)
                return
    if temp == 0:
        white += 1
        return
    else:
        blue += 1
        return

re(0, 0, N)
print(white)
print(blue)