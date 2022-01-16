# BOJ_2217
# 로프

N=int(input())

ropes=[]
for _ in range(N):
    rope=int(input())
    ropes.append(rope)

ropes.sort(reverse=True)

for i in range(len(ropes)):
    ropes[i]*=i+1
print(max(ropes))
