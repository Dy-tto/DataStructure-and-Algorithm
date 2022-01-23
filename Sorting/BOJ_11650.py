# BOJ No.11650
# 좌표 정렬하기

import sys

n=int(sys.stdin.readline())

points=[]

for _ in range(n):
    x,y=map(int,sys.stdin.readline().split())
    points.append((x,y))
points.sort(key=lambda x: (x[0],x[1]))

for i in range(len(points)):
    print(points[i][0], points[i][1],sep=' ')
