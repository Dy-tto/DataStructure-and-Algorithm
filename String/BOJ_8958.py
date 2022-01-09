# BOJ No.10809
# 알파벳 찾기

s=list(input())

# a~z의 위치를 저장할 리스트 생성
result=[-1]*(ord('z')-ord('a')+1)

# 각 알파벳이 처음 나오는 index 저장
for i in s:
    result[ord(i)-ord('a')]=s.index(i)

for i in range(len(result)):
    print(result[i],end=' ')
