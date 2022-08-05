import sys

N = int(sys.stdin.readline())
arr = []
MAXtemp = [0, 0, 0]
MINtemp = [0, 0, 0]
MAXdp = [0, 0, 0]
MINdp = [0, 0, 0]

for i in range(N):
    arr = (list(map(int, sys.stdin.readline().split())))

    for j in range(3):
        if j == 0:
            MAXdp[0] = arr[0] + max(MAXtemp[j], MAXtemp[j + 1])
        elif j == 1:
            MAXdp[1] = arr[1] + max(MAXtemp[j - 1], MAXtemp[j], MAXtemp[j + 1])
        else:
            MAXdp[2] = arr[2] + max(MAXtemp[j], MAXtemp[j - 1])
    MAXtemp = MAXdp[:]

    for j in range(3):
        if j == 0:
            MINdp[0] = arr[0] + min(MINtemp[j], MINtemp[j + 1])
        elif j == 1:
            MINdp[1] = arr[1] + min(MINtemp[j - 1], MINtemp[j], MINtemp[j + 1])
        else:
            MINdp[2] = arr[2] + min(MINtemp[j], MINtemp[j - 1])
    MINtemp = MINdp[:]

print(max(MAXdp), min(MINdp))