# BOJ No.10808
# 알파벳 개수

lst=[0]*26

s=input()
for i in s:
    lst[ord(i)-ord('a')]+=1
for l in lst:
    print(l,end=' ')
