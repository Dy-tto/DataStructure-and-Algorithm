# BOJ No.1026
# 보물

N=int(input())

A=list(map(int,input().split()))
B=list(map(int,input().split()))

A.sort(reverse=True)
B.sort()

AB=[A[x]*B[x] for x in range(N)]
S=sum(AB)
print(S)
