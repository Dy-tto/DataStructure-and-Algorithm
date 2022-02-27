# BOJ No.1912
# 연속합

n=int(input())
d=[-1000]*(n+1)
nums=list(map(int,input().split()))
d[1]=nums[0]

for i in range(2,n+1):
    d[i]=max(nums[i-1],d[i-1]+nums[i-1])
print(max(d))

