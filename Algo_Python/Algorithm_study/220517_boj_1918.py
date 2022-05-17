import sys


arr = list(sys.stdin.readline()) 
stack=[] 
result ='' 
for i in arr: 
    if i.isalpha(): 
        result+= i
    else: 
        if i == '(': 
            stack.append(i) 
        elif i == '*' or i == '/': 
            while stack and (stack[-1] == '*' or stack[-1] =='/'): 
                result += stack.pop() 
            stack.append(i) 
        elif i == '+' or i == '-': 
            while stack and stack[-1] != '(': 
                result+= stack.pop() 
            stack.append(i) 
        elif i == ')': 
            while stack and stack[-1] != '(': 
                result += stack.pop() 
            stack.pop() 
while stack : 
    result+=stack.pop() 
print(result)