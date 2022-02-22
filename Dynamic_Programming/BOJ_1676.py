# BOJ No.1676
# 팩토리얼 0의 개수

d=[1]*501
n=int(input())
for i in range(1,n+1):
    d[i]=d[i-1]*i
cnt=0
for j in str(d[n])[::-1]:
    if j=='0':
        cnt+=1
    else:
        print(cnt)
        break

