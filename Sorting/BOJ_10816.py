# BOJ No.10816
# 숫자 카드 2

from collections import Counter

n=int(input())
cnt=Counter(list(map(int,input().split())))
m=int(input())
lst=[num for num in list(map(int,input().split()))]
for num in lst:
    if num in cnt:
        print(cnt[num],end=' ')
    else:
        print(0,end=' ')
