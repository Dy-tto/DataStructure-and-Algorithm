
# BOJ No.11729
# 하노이 탑 이동 순서

def hanoi(n,from_pos,to_pos,mid):
    if n==1:
        path.append((from_pos,to_pos))
        return
    hanoi(n-1,from_pos,mid,to_pos)
    path.append((from_pos,to_pos))
    hanoi(n-1,mid,to_pos,from_pos)

N=int(input())

path=[]
hanoi(N,1,3,2)
print(len(path))
for i in path:
    print(i[0],i[1])
