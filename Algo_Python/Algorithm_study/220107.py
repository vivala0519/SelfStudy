courses = ['aeb-1305', 'site-1305', 'play-1215', 'web-1304', 'site-1304', 'beb-1305']
for i in range(len(courses)):
    courses[i] = courses[i].split('-')
courses.sort(key=lambda x : (x[1], x[0]))
print(courses)
for i in range(len(courses)):
    courses[i] = ''.join(courses[i][0] + '-' +courses[i][1])
print(courses)