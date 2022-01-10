# 이코테 그리디 알고리즘
# 모험가 길드

N=int(input())

lst=list(map(int,input().split()))
lst.sort()
result=0 # 총 그룹 수
count=0 # 현재 그룹에 포함된 모험가의 수

for i in lst: # 공포도를 낮은 것부터 하나씩 확인
    count+=1 # 현재 그룹에 해당 모험가 포함
    if count>=i: # 현재 그룹에 포함된 모험가의 수가 현재 공포도 이상일 때
        result+=1
        count=0
print(result)
