# BOJ No.1049
# 기타줄

n,m=map(int,input().split())
lst=[]
total=0
for _ in range(m):
    package, unit=map(int,input().split())
    lst.append((package,unit))
min_package=sorted(lst,key=lambda x :x[0])[0][0]
min_unit=sorted(lst,key=lambda x :x[1])[0][1]

total=min(min_package*(n//6)+min_unit*(n%6),
          min_unit*n,
          min_package*((n//6)+1))

print(total)
