# BOJ No.18870
# 좌표 압축

import sys

n=int(sys.stdin.readline())
nums=list(map(int,sys.stdin.readline().split()))
set_nums=set(nums)
sorted_nums=sorted(set_nums)
cnt={sorted_nums[i]:i for i in range(len(sorted_nums))}
for n in nums:
    print(cnt[n],end=' ')
