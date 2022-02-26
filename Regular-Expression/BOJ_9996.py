# BOJ No.9996
# 한국이 그리울 땐 서버에 접속하지

import re

n=int(input())
start,end=input().rstrip().split('*')
pattern=''.join(start+'+.*'+end+'{1}$')
regex=re.compile(pattern)
for _ in range(n):
    text=input().rstrip()
    m=regex.match(text)
    if m:
        print("DA")
    else:
        print("NE")
