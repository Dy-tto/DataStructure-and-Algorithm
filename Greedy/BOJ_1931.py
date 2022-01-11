# BOJ No.1931
# 회의실 배정

import sys
N=int(sys.stdin.readline())

times=[]

for _ in range(N):
    time=list(map(int,sys.stdin.readline().split()))
    times.append(time)

times=sorted(times,key=lambda x : (x[1],x[0]))

current=times[0][1]
count=1

for i in range(1,N):
    if times[i][0]>=current:
        count+=1
        current=times[i][1]
print(count)
