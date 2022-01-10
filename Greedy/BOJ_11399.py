# BOJ No.11399
# ATM

N=int(input())

p=list(map(int,input().split()))

p.sort()

count=0
result=0
for i in p: # 필요한 시간의 합의 최솟값을 구하려면 필요한 시간을 오름차순으로 정렬하면 됨
    result+=i+count
    count+=i
print(result)
