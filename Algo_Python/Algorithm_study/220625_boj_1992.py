import sys

n = int(sys.stdin.readline())
lst = []
for _ in range(n):
    lst.append(list(map(int, sys.stdin.readline().rstrip())))

def quad(x, y, N):
    one = lst[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if one != lst[i][j]:
                print("(", end="")
                quad(x, y, N//2)
                quad(x, y+N//2, N//2)
                quad(x+N//2, y, N//2)
                quad(x+N//2, y+N//2, N//2)
                print(")", end="")
                return
    if one == 0:
        print(0, end="")
    else:
        print(1, end="")

quad(0, 0, len(lst))