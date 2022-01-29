# BOJ No.10809
# 알파벳 찾기

s=list(input())

result=[-1]*(ord('z')-ord('a')+1)

for i in s:
    result[ord(i)-ord('a')]=s.index(i)

for i in range(len(result)):
    print(result[i],end=' ')
