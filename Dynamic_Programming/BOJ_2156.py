# BOJ No.2156
# 포도주 시식

n=int(input())
dp=[0]*10001
lst=[0]*10001
for i in range(n):
    lst[i]=int(input())
dp[0]=lst[0]

dp[1]=lst[0]+lst[1]
dp[2]=max(lst[2]+lst[0],lst[2]+lst[1],dp[1])
for i in range(3,n):
    dp[i]=max(dp[i-1],dp[i-3]+lst[i-1]+lst[i],dp[i-2]+lst[i])

print(max(dp))
