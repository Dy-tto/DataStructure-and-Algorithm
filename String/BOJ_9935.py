# BOJ No.9935
# 문자열 폭발

import sys

s=sys.stdin.readline().rstrip()
bomb=sys.stdin.readline().rstrip()
lst=[]
length = len(bomb)
for i in s:
    lst.append(i)
    if bomb[-1] == i and ''.join(lst[-length:]) == bomb:
        del lst[-length:]

'''
while bomb in s:
    s=s.replace(bomb,'')
'''
if lst==[]:
    print("FRULA")
else:
    print(''.join(lst))

