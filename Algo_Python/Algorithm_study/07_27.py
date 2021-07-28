string = 'gbgbh'
for last in range(0, string.__len__()):
    res = ''
    ok = False;
    change = ''
    if string.__len__() > 1:
        for i in range(0, string.__len__()-1):
            for j in range(1, string.__len__()):
                if i + j < string.__len__():
                    if string[i] == string[i+j]:
                        for k in range(0, string.__len__()):
                            if(string.__len__() == 2):
                                res = string[k]
                            else:
                                if k == i:
                                    pass
                                elif k == i+j:
                                    pass
                                else:
                                    res += string[k]
                                    if string[i] == 'z':
                                        change = 'a'
                                    else:
                                        change = chr(ord(string[i]) + 1)

                        change += res
                        string = change
                        ok = True;
                        break
            if ok == True:
                break;
    else:
        break;



print(string)