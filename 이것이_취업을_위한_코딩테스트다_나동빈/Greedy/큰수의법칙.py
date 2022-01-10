# 이코테 그리디 알고리즘
# 실전문제 1) 큰 수의 법칙

N,M,K=map(int,input().split())

nums=list(map(int,input().split()))
nums=sorted(nums)
first=nums[-1]
second=nums[-2]

result=0
count=0

count=int(M//(K+1))*K + M%(K+1)

result+=first*count + (M-count)*second
print(result)
