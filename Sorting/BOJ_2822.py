# BOJ No.2822
# 점수 계산

scores=[]

for i in range(8):
    score=int(input())
    scores.append((score,i+1))
scores.sort(key=lambda x : -x[0])
total=0
for i in range(5):
    total+=scores[i][0]
lst=sorted(scores[:5],key=lambda x : x[1])
print(total)
for i in range(5):
    print(lst[i][1],end=' ')

