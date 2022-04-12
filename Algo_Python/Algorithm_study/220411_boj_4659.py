import sys

aeiou = ['a', 'e', 'i', 'o', 'u']

while True:
    result = []
    s = sys.stdin.readline().rstrip()
    if s == 'end':
        break
    cnt = 0
    # aeiou_cnt = 0
    # notaeiou_cnt = 0
    # temp = ''
    # result = True
    # for i in s:
    #     if i in aeiou:
    #         notaeiou_cnt = 0
    #         aeiou_cnt += 1
    #         cnt += 1
    #         if aeiou_cnt >= 3:
    #             result = False
    #         if temp == i:
    #             if i == 'e' or i == 'o':
    #                 pass
    #             else:
    #                 result = False
    #     else:
    #         aeiou_cnt = 0
    #         notaeiou_cnt += 1
    #         if notaeiou_cnt >= 3:
    #             result = False
    #         if temp == i:
    #             result = False
    #     temp = i
    # if cnt < 1:
    #     result = False
    #
    # if result is False:
    #     print('<' + s + '> is not acceptable')
    # else:
    #     print('<' + s + '> is acceptable')
    for i in s:
        if i in aeiou:
            cnt += 1
    if cnt == 0:
        result.append(False)
    else:
        for i in range(0, len(s)-2):
            temp = s[i:i+3]
            cnt = 0
            for j in temp:
                if j in aeiou:
                    cnt += 1
            if cnt == 3 or cnt == 0:
                # ('<' + s + '> is not acceptable')
                result.append(False)
    for i in range(0, len(s) - 1):
        if s[i] == s[i+1]:
            if s[i] == 'e' or s[i] == 'o':
                pass
            else:
                result.append(False)
    if False in result:
        print('<' + s + '> is not acceptable.')
    else:
        print('<' + s + '> is acceptable.')