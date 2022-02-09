# BOJ No.2864
# 5와 6의 차이

a,b=input().split()

min_value=0
max_value=0

lst_a=list(a)
lst_b=list(b)
place=0
while True:
    if lst_a!=[]:
        if lst_a[-1]=='5' or lst_a[-1]=='6':
            min_value+=5*(10**place)
            max_value+=6*(10**place)
            lst_a.pop()
        else:
            min_value+=int(lst_a[-1])*(10**place)
            max_value+=int(lst_a[-1])*(10**place)
            lst_a.pop()
    if lst_b!=[]:
        if lst_b[-1]=='5' or lst_b[-1]=='6':
            min_value+=5*(10**place)
            max_value+=6*(10**place)
            lst_b.pop()
        else:
            min_value+=int(lst_b[-1])*(10**place)
            max_value+=int(lst_b[-1])*(10**place)
            lst_b.pop()
    place+=1
    if lst_a==[] and lst_b==[]:
        break
print(min_value,max_value)
