N=input()

lst=list(N)

lst.sort()

cnt=0
for i in range(1,len(lst)):
    temp=sorted(lst)
    for j in range(i,len(lst)):
        answer=int(''.join(sorted(temp,reverse=True))[:])
        cnt+=1
        if answer%30==0:
            print(answer,'3')
            break
        if cnt==len(lst):
            print(-1,'4')
            break
        temp[i],temp[j]=temp[j],temp[i]
        print(temp,'2')

