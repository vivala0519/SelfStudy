a = '\t'
b = 'Z'
if a.isalpha() == False or b.isalpha() == False:
    print(-1)
elif a.isupper() == b.isupper():
    print(1)
elif a.islower() == b.islower():
    print(1)
else:
    print(0)