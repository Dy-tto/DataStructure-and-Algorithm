# BOJ No.1316
# 그룹 단어 체커

N=int(input())
count=0

for _ in range(N):
    word=list(input())
    checker=[0]*(ord('z')-ord('a')+1)
    for i in range(len(word)):
        if checker[ord(word[i])-ord('a')]==0:
            checker[ord(word[i])-ord('a')]+=1
        elif checker[ord(word[i])-ord('a')]>0 \
            and word[i]!=word[i-1]:
            checker[ord(word[i])-ord('a')]=-1
            break

    if checker.count(-1)==0:
        count+=1
print(count)
