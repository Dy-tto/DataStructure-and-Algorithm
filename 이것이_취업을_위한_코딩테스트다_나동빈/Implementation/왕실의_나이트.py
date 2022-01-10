# 이코테 구현 알고리즘
# 예제2) 왕실의 나이트

loc=input()
col=int(ord(loc[0]))-int(ord('a')) + 1 # 문자형태의 열을 숫자로 변환
row=int(loc[1])

moves=[(-2,-1),(-2,1),(1,-2),(1,2),(2,-1),(2,1),(-1,2),(-1,-2)]

count=0

for move in moves:
    next_row=row+move[0]
    next_col=col+move[1]

    if next_row<1 or next_col<1 or next_row>8 or next_col>8:
        continue
    else:
        count+=1
print(count)

