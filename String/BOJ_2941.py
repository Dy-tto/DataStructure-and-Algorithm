# BOJ No.1065
# 한수

def func(n:int)->bool:
    if n<100:
        return True
    num=list(str(n))
    d=int(num[1])-int(num[0]) # 공차
    for i in range(1,len(num)): # 각 자리 수가 등차수열인지 검사
        if int(num[i])-int(num[i-1])!=d:
            return False
    return True

N=int(input())
count=0
for i in range(1,N+1):
    if func(i)==True:
        count+=1

print(count)
