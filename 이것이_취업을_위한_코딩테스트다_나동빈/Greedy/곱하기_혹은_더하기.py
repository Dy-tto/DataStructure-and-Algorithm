# 이코테 그리디 알고리즘
# 곱하기 혹은 더하기

S=list(input())

result=int(S[0])

for i in range(1,len(S)):
    if result<=1:
        result+=int(S[i])
    elif int(S[i])<=1:
        result+=int(S[i])
    else:
        result*=int(S[i])
print(result)


