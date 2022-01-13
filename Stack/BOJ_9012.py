# BOJ_9012
# 괄호

T=int(input())

for _ in range(T):
    lst=[]
    result=True
    string=input()
    for i in string:
        if i=='(':
            lst.append(i)
        elif i==')':
            if len(lst)==0:
                result=False
                break
            else:
                lst.pop()
    if result==True and len(lst)==0:
        print("YES")
    else:
        print("NO")
