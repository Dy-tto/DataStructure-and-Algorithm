# BOJ No.11652
# 카드

import sys

n=int(sys.stdin.readline())
cards={}
for i in range(n):
    card=int(sys.stdin.readline())
    if card in cards:
        cards[card]+=1
    else:
        cards[card]=1
result=sorted(cards.items(),key=lambda x : (-x[1],x[0]))
print(result[0][0])
