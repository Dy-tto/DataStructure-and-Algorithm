# BOJ No.1946
# ė ėėŽė

import sys

T=int(input())
for t in range(T):
    N=int(input())
    applicants=[]
    cnt=1
    for n in range(N):
        applicant=list(map(int,sys.stdin.readline().split()))
        applicants.append(applicant)
    applicants.sort()
    max_num=applicants[0][1]
    for i in range(1,N):
        if max_num>applicants[i][1]:
            cnt+=1
            max_num=applicants[i][1]
    print(cnt)

