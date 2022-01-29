# BOJ No.4948
# 베르트랑 공준

import sys

def era(N):
    checker=[True]*2*N
    prime=[]

    for i in range(2,N+1):
        if checker[i]==True:
            prime.append(i)
            for j in range(i**2,N,i):
                checker[j]=False
    return prime

while True:
    T=int(sys.stdin.readline())
    if T==0:
        break
    lst=era(2*T+1)
    ans=[]

    for n in lst:
        if n>T and n<=2*T:
            ans.append(n)

    print(len(ans))


