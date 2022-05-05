words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

arr = []
result = []
for i in queries:
    right = len(i) - 1
    left = 0
    cnt = 0
    if i[0] == '?':
        while i[right] != '?':
            right -= 1
        print(right, i[right + 1:])
        for j in words:
            if len(j) == len(i):
                if j[right + 1:] == i[right + 1:]:
                    cnt += 1
        result.append(cnt)
    else:
        while i[left] != '?':
            left += 1
        print(left, i[:left])
        for j in words:
            if len(j) == len(i):
                if j[:left] == i[:left]:
                    cnt += 1
        result.append(cnt)
print(result)