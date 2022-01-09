# BOJ No.4673
# 셀프 넘버

def d(n:int) -> int:
    new_num=n
    for i in str(n):
        new_num+=int(i)
    return new_num

numbers=set(range(1,10000))
generated_num=set()

for i in range(1,10000):
    generated_num.add(d(i))

self_num=sorted(numbers-generated_num)

for j in range(len(self_num)):
    print(self_num[j])

