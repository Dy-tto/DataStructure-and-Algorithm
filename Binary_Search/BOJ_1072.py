# BOJ No.1072
# 게임

x,y=map(int,input().split())

z=(y*100)//x

if z>=99:
    print(-1)
else:
    answer=0
    start=1
    end=x

    while start<=end:
        mid=(start+end)//2
        nz=(y+mid)*100//(x+mid)
        if nz<=z:
            start=mid+1
        else:
            answer=mid
            end=mid-1
    print(answer)
