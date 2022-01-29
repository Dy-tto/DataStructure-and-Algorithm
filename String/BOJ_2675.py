# BOJ No.2675
# 문자열 반복

T=int(input())

for i in range(T):
    R, S=input().split()
    for j in range(len(S)):
        print(S[j]*int(R),end='')
    print('')
