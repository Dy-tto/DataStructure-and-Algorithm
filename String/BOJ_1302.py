# BOJ No.1302
# 베스트셀러

from collections import Counter

n=int(input())
lst=[]
for i in range(n):
    lst.append(input())
cnt=Counter(lst)
result=cnt.most_common()
result.sort(key=lambda x : (-x[1],x[0]))
print(result[0][0])
