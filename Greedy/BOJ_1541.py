# BOJ No.1541
# 읽어버린 괄호

eqn=input().split('-')
result=0
for i in eqn[0].split('+'):
    result+=int(i)
for i in range(1,len(eqn)):
    for j in eqn[i].split('+'):
        result-=int(j)

print(result)
