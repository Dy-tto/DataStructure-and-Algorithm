# BOJ No.2749
# 피보나치 수 3
# 피사노 주기 이용

def fib(n):
    dp=[0]*(n+1)
    dp[1]=1
    for i in range(2,n+1):
        dp[i]=(dp[i-1]+dp[i-2])%m
    return dp[n]
n=int(input())
m=10**6
pisano=15*(m//10)
print(fib(n%pisano))
