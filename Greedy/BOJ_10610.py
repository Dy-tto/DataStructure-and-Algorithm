# BOJ_10610
# 30

import sys
N=list(sys.stdin.readline().rstrip())
S=0
N.sort()
for i in N:
    S+=int(i)
if N[0]!='0' or S%3!=0:
    print(-1)
else:
    N.sort(reverse=True)
    print(''.join(N))



