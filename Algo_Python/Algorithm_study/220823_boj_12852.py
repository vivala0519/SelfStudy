import sys

N = int(sys.stdin.readline())
cnt = [[0, []] for _ in range(N + 1)]
cnt[1][0] = 0
cnt[1][1] = [1]

for i in range(2, N + 1):
    cnt[i][0] = cnt[i - 1][0] + 1
    cnt[i][1] = cnt[i - 1][1] + [i]

    if i % 3 == 0 and cnt[i // 3][0] + 1 < cnt[i][0]:
        cnt[i][0] = cnt[i // 3][0] + 1
        cnt[i][1] = cnt[i // 3][1] + [i]

    if i % 2 == 0 and cnt[i // 2][0] + 1 < cnt[i][0]:
        cnt[i][0] = cnt[i // 2][0] + 1
        cnt[i][1] = cnt[i // 2][1] + [i]

print(cnt[N][0])
for i in cnt[N][1][::-1]:
    print(i, end=' ')