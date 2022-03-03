# BOJ No.17219
# 비밀번호 찾기

n,m=map(int,input().split())

dic={}
for i in range(n):
    add,pwd=input().split()
    dic[add]=pwd

for j in range(m):
    p=input()
    print(dic[p])
