# BOJ No.11004
# K번째 수

n,k=map(int,input().split())

lst=[x for x in map(int,input().split())]
lst.sort()
print(lst[k-1])
