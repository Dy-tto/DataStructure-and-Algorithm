# BOJ No.1003
# 피보나치 함수

t=int(input())

for _ in range(t):
    n=int(input())
    d0=[0]*(n+1)
    d1=[0]*(n+1)
    if n==0:
        print(1,0)
    elif n==1:
        print(0,1)
    else:
        d1[0]=0
        d1[1]=1
        d0[0]=1
        d0[1]=0
        d0[2]=1

        for i in range(2,n+1):
            d1[i]=d1[i-1]+d1[i-2]
        for j in range(3,n+1):
            d0[j]=d0[j-1]+d0[j-2]

        print(d0[n],d1[n])
