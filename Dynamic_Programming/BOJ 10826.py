# BOJ 10826
# 피보나치 수 4

def fib(n):
    dp=[0]*(10000+1)
    dp[1]=1
    for i in range(2,n+1):
        dp[i]=(dp[i-1]+dp[i-2])
    return dp[n]
n=int(input())
print(fib(n))
