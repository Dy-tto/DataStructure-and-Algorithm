# BOJ No.1100
# 하얀 칸

cnt=0
chess=[]
for i in range(8):
    chess.append(list(input()))
for i in range(8):
    for j in range(8):
        if (i+j)%2==0 and chess[i][j]=='F':
            cnt+=1
print(cnt)
