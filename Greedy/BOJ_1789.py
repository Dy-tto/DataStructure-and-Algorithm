# BOJ_1789
# 수들의 합

S=int(input())
n=0
i=1
while True:
    if S==0 or S<i:
        break
    if S>=i:
        S-=i
        n+=1
        i+=1

print(n)
