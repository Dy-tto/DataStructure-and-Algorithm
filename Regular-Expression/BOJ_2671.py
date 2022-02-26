# BOJ No.2671
# 잠수함식별

import re

pattern='(100+1+|01)+'

regex=re.compile(pattern)
text=input().rstrip()

m=regex.fullmatch(text)

if m:
    print("SUBMARINE")
else:
    print("NOISE")
