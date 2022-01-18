# BOJ_2108
# 통계학

from collections import Counter
import sys
N=int(sys.stdin.readline())
lst=[]
for i in range(N):
    lst.append(int(sys.stdin.readline()))
lst.sort()
avg=round((sum(lst)/N))
median=lst[N//2]
mode=Counter(lst).most_common()
ran=lst[-1]-lst[0]
if len(mode)>1:
    if mode[0][1]==mode[1][1]:
        mode=mode[1][0]
    else:
        mode=mode[0][0]
else:
    mode=mode[0][0]
print(avg,median,mode,ran,sep='\n',end='')
