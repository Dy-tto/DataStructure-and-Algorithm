# BOJ No.9342
# 염색체

import re
t=int(input())

regex=re.compile('^[A-F]{0,1}A+F+C+[A-F]{0,1}$')

for i in range(t):
    text=input()

    m=regex.match(text)
    if m:
        print("Infected!")
    else:
        print("Good")
