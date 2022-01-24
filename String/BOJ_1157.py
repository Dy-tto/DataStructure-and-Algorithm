# BOJ_1157
# 단어 공부

S=input()
S=S.upper()
distinct_s=set(S)
dict_s={}
for i in distinct_s:
    dict_s[i]=S.count(i)
max_cnt=max(dict_s.values())

result=[]
for key,value in dict_s.items():
    if dict_s[key]==max_cnt:
        result.append(key)
if len(result)>1:
    print('?')
else:
    print(result[0])
