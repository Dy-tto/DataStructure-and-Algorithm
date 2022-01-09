# BOJ No.2798
# 블랙잭

N,M=map(int,input().split())

lst=list(map(int,input().split()))
lst=sorted(lst)

max=sum(lst[:3])

for i in range(0,N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if lst[i]+lst[j]+lst[k]>max \
                    and lst[i]+lst[j]+lst[k]<=M:
                max=lst[i]+lst[j]+lst[k]
print(max)
