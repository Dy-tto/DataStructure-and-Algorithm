# BOJ No.1013
# Contact

import re
t=int(input())
pattern='(100+1+|01)+'

regex=re.compile(pattern)

for i in range(t):
    text=input().rstrip()

    m=regex.fullmatch(text)

    if m:
        print("YES")
    else:
        print("NO")
