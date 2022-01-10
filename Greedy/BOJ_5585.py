# BOJ No.5585
# 거스름돈

price=int(input())

changes=[500, 100, 50, 10, 5, 1]

left=1000-price

count=0
for m in changes:
    count+=left//m
    left%=m
print(count)
