# BOJ No.8958
# OX퀴즈

T=int(input())

result=[0]*T

for i in range(T):
    count=0
    case=list(input())
    for j in range(len(case)):
        if case[j]=='O':
            result[i]+=(1+count)
            count+=1
        else:
            count=0


for k in range(len(result)):
    print(result[k])

