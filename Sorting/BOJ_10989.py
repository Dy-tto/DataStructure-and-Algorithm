# BOJ No.10989
# 수 정렬하기 3

import sys

n=int(sys.stdin.readline())
cnt=[0] * 10001

for _ in range(n):
    num=int(sys.stdin.readline())
    cnt[num]+=1
for i in range(len(cnt)):
    for j in range(cnt[i]):
        print(i)
