# BOJ No.4796
# 캠핑

case=0

while True:
    l,p,v=map(int,input().split())
    if l==0 and p==0 and v==0:
        break
    camp=0
    case+=1
    while v>0:
        if v>=p:
            v-=p
            camp+=l
        elif v>=l:
            v-=p
            camp+=l
        else:
            camp+=v
            v-=p
    print(f'Case {case}: {camp}')




