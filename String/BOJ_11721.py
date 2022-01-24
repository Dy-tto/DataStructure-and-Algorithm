lst=[0]*23

s=input()
for i in s:
    lst[ord(i)-ord('a')]+=1
for l in lst:
    print(l,end=' ')
