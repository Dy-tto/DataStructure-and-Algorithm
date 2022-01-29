# Count Sort

# 모든 원소의 값이 0보다 크거나 같다고 가정
lst=[7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
cnt=[0]*(max(lst)+1)

for i in lst:
    cnt[i]+=1 # 각 데이터에 해당하는 인덱스의 값 증가
for j in range(len(cnt)): # 리스트에 기록된 정렬 정보 확인
    for k in range(cnt[j]):
        print(j,end=' ')
