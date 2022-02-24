# BOJ No.5637
# 가장 긴 단어

import re
text=[]
while True:
    text.extend(input().split())
    if text[-1]=='E-N-D':
        break

regex=[re.sub('[^a-z-]','',x.lower()) for x in text]
regex.sort(key=lambda x : len(x), reverse=True)
print(regex[0])
