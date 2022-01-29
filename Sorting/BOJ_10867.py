# BOJ No.10867
# 중복 빼고 정렬하기

n=int(input())
lst=list(set(map(int,input().split())))
lst.sort()
for i in lst:
    print(i,end=' ')
