# BOJ No.1065
# 한 수

def func(n:int)->bool:
    if n<100:
        return True
    num=list(str(n))
    d=int(num[1])-int(num[0])
    for i in range(1,len(num)):
        if int(num[i])-int(num[i-1])!=d:
            return False
    return True

N=int(input())
count=0
for i in range(1,N+1):
    if func(i)==True:
        count+=1

print(count)
