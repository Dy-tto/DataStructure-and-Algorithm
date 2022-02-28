# Programmers
# Hash - 완주하지 못한 선수

from collections import Counter
def solution(participant, completion):
    p=Counter(participant)
    c=Counter(completion)
    for i in p.keys():
        if c[i]==False or p[i] != c[i]:
            answer=i
    return answer
