# 이코테 구현 알고리즘
# 예제1) 상하좌우

N=int(input())

plan=list(input().split())

x,y=1,1 # 시작 위치

# 방향 벡터 L R U D
dx=[0,0,-1,1]
dy=[-1,1,0,0]
move=['L', 'R', 'U', 'D']

for i in plan:
    for j in range(len(move)):
        if i==move[j]:
            nx=x+dx[j] # 범위 안에 있는지 검사 전 temp 변수
            ny=y+dy[j]
    if nx<1 or ny<1 or nx>N or ny>N: # 범위를 벗어나는지 검사
        continue
    x=nx
    y=ny
print(x,y)


