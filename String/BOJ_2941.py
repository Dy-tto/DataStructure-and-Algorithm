# BOJ No.2941
# 크로아티아 알파벳

cro=['c=','c-','dz=','d-','lj','nj','s=','z=']

count=0

word=input()

for i in cro:
    if i in word:
        count+=word.count(i)
        word=word.replace(i,' ')
word=word.replace(' ','')
print(count+len(word))

