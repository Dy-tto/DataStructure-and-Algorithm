# BOJ_10162
# 전자레인지

T=int(input())

buttons=[300,60,10]
cnt=[0]*3
if T%buttons[2]!=0:
    print(-1)
else:
    for i in range(len(buttons)):
        if T//buttons[i]!=0:
            cnt[i]+=T//buttons[i]
            T%=buttons[i]

    for j in cnt:
        print(j,end=' ')
