# BOJ No.2929
# 머신 코드

import re

text=input()

regex=re.split('(?=[A-Z])',text)
cnt=0
for i in range(1,len(regex)-1):
    if len(regex[i])%4 !=0:
        cnt+=4-len(regex[i])%4
print(cnt)
