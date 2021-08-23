table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
         "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
         "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["PYTHON", "C++", "SQL"]
preference = [7, 5, 5]
total = 0
score = []
dic = {}
for i in table:
    i = i.split(' ')        # 직업군 언어점수 리스트화
    total = 0
    for j in range(1, i.__len__()):     # 직업군별 언어선호도 점수 체크
        for lan in range(0, languages.__len__()):
            if languages[lan] == i[j]:
                if j == 1:
                    sc = 5
                elif j == 2:
                    sc = 4
                elif j == 3:
                    sc = 3
                elif j == 4:
                    sc = 2
                elif j == 5:
                    sc = 1
                total += sc * preference[lan]
            else:
                total += 0
    dic[i[0]] = total       # 직업군별 총합 점수
print(dic)
answer_list = [k for k, v in dic.items() if v == max(dic.values())]     # 최대값 리스트
print(answer_list)
answer_list.sort()      # 사전순 정렬
answer = answer_list[0]
print(answer)