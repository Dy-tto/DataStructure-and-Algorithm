# BOJ No.1436
# 영화감독 숌

n=int(input())
cnt=0
num=1
len_num=len(list(str(num)))
while True:
    if cnt==n:
        print(num)
        break
    num+=1
    if '666' in str(num):
        cnt+=1

