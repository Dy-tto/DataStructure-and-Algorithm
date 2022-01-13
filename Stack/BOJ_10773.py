# BOJ_10773
# 제로

K=int(input())

answer=[]

for i in range(K):
    num=int(input())
    if num!=0:
        answer.append(num)
    else:
        answer.pop()
print(sum(answer))
