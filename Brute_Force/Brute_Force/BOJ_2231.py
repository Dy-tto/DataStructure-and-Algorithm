# BOJ No.2231
# 분해합

N=int(input())

check=True
for i in range(N):
    ans=0
    temp=list(str(i))

    for j in temp:
        ans+=int(j)
    ans+=i
    if ans==N:
        print(i)
        check=False
        break
if check==True:
    print(0)

