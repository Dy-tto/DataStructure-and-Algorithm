# BOJ No.11721
# 열 개씩 끊어 출력하기

s=input()
cnt=0
for i in s:
    print(i,end='')
    cnt+=1
    if cnt%10==0:
        print()
