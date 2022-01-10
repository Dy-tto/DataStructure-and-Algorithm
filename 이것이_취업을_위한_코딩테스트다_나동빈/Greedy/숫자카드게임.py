# 이코테 그리디 알고리즘
# 실전문제 2) 숫자 카드 게임

N, M=map(int,input().split())

lst=[]

for col in range(N):
    row=list(map(int,input().split()))
    lst.append(row)

cmp=min(lst[0])

for i in lst:
    if min(i)>cmp:
        cmp=min(i)
print(cmp)
