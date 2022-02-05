# BOJ No.2579
# 계단 오르기

n=int(input())

dp=[0]*301
scores=[0]
for i in range(1,n+1):
    scores.append(int(input()))
dp[1]=scores[1]
if n>1:
    dp[2]=scores[1]+scores[2]
    for i in range(3,n+1):
        dp[i]=max(dp[i-2],dp[i-3]+scores[i-1]+scores[i],dp[i-2]+scores[i])

print(dp[n])
