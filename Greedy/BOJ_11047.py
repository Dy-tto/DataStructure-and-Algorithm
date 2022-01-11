# BOJ No.11047
# 동전 0

N,K=map(int,input().split())

coins=[]
count=0

for i in range(N):
    coin=int(input())
    coins.append(coin)

coins=sorted(coins,reverse=True)

for coin in coins:
    if K//coin!=0:
        count+=K//coin
        K%=coin
print(count)
