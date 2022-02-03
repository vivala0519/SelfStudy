files =  ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
for i in range(len(files)):
    for j in range(len(files[i])):
        if files[i][j].isnumeric():
            files[i] = [files[i][:j], files[i][j:]]
            break
# print(files)
for i in range(len(files)):
    for j in range(len(files[i][1])):
        # print(files[i][1][j])
        if files[i][1][j].isdigit() is False:
            files[i] = [files[i][0], files[i][1][:j], files[i][1][j:]]
            break
print(files)
files.sort(key=lambda x: (x[0].upper(),int(x[1])))
print(files)
for i in range(len(files)):
    files[i] = ''.join(files[i])
print(files)