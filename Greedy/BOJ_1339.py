# BOJ No.1339
# 단어 수학

n=int(input())
words=[]
alphabet='abcdefghijklmnopqrstuvwxyz'
for _ in range(n):
    word=input()
    words.append(list(word))
dicts={x:0 for x in alphabet.upper()}
# 알파벳의 자리 수에 해당하는 만큼 10의 거듭제곱 수를 더해줌
for i in range(len(words)):
    words[i]=words[i][::-1]
    for j in range(len(words[i])):
        dicts[words[i][j]]+=10**j
result=0
lst=[]

for value in dicts.values():
    lst.append(value)
lst.sort(reverse=True)
m=9
# 1~9까지 값의 크기 순으로 분배
while m>0:
    for i in lst:
        result+=i*m
        m-=1
print(result)
