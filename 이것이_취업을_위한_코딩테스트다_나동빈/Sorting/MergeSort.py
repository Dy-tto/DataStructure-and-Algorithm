# MergeSort

def mergesort(lst):
    n=len(lst)
    if n<=1:
        return lst
    else:
        mid=n//2
        U=mergesort(lst[:mid])
        V=mergesort(lst[mid:])
        return merge(U,V)
def merge(U,V):
    s=[]
    i=0
    j=0
    while i<len(U) and j<len(V):
        if U[i]<V[j]:
            s.append(U[i])
            i+=1
        else:
            s.append(V[j])
            j+=1
    if i<len(U):
        s+=U[i:]
    else:
        s+=V[j:]
    return s

def mergesort2(lst2,start,end):
    if start<end:
        mid=(start+end)//2
        mergesort2(lst2,start,mid)
        mergesort2(lst2,mid+1,end)
        merge2(lst2,start,mid,end)
def merge2(lst2,start,mid,end):
    U=[]
    i=start
    j=mid+1
    while i<=mid and j<=end:
        if lst2[i]<lst2[j]:
            U.append(lst2[i])
            i+=1
        else:
            U.append(lst2[j])
            j+=1
    if i<=mid:
        U+=lst2[i:mid+1]
    else:
        U+=lst2[j:end+1]
    for k in range(start,end+1):
        lst2[k]=U[k-start]

lst=[27,10,12,20,25,13,15,22]
lst2=[27,10,12,20,25,13,15,22]
print(mergesort(lst))
mergesort2(lst2,0,len(lst2)-1)
print(lst2)
