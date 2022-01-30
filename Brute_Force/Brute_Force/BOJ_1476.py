# BOJ No.1476
# 날짜 계산

e, s, m=map(int,input().split())
ne,ns,nm,year=1,1,1,1
while True:
    if ne==e and ns==s and nm==m:
        print(year)
        break
    year+=1
    ne+=1
    ns+=1
    nm+=1
    if ne>=16:
        ne-=15
    if ns>=29:
        ns-=28
    if nm>=20:
        nm-=19
