strng = 'abcd\nefgh\nijkl\nmnop'
k = 2
v = 3
arr = []
for i in range(0, strng.__len__()):     # 문자열 길이동안 배열에 넣기
    if strng[i] == '\n':                # 줄바꿈이라면 한번만
        arr.append(strng[i])
    else:
        for j in range(0, k):           # 각 문자를 k만큼 반복하여 배열에 넣기
            arr.append(strng[i])
after_horizon = ''.join(arr)            # 배열을 다시 문자열화
for_vertical = after_horizon.split('\n')    # 두번째 작업을 위해 줄바꿈단위로 스플릿
arr = []
for i in range(0, for_vertical.__len__()):      # 배열화 하며 중간에 줄바꿈 모두 하되 마지막엔 안하기
    if i == for_vertical.__len__()-1:
        arr.append(for_vertical[i])
    else:
        arr.append(for_vertical[i])
        arr.append('\n')
final = []
for i in range(0, arr.__len__()):       # v만큼 각 배열 반복하되 중간에 줄바꿈하기(마지막x)
    if arr[i] == '\n':
        continue
    else:
        for j in range(0, v):
            final.append(arr[i])
            if j == v-1:
                continue
            else:
                final.append('\n')
    if i == arr.__len__()-1:
        continue
    else:
        final.append('\n')
result = ''.join(final)         # 결과 문자열화
print(result)