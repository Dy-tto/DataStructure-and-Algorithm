# 이코테 그리디 알고리즘
# 모험가 길드

N=int(input())

lst=list(map(int,input().split()))
lst.sort()
result=0 # 총 그룹 수
count=0 # 현재 그룹에 포함된 모험가의 수

for i in lst:
    count+=1
    if count>=i:
        result+=1
        count=0
print(result)



