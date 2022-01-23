from itertools import combinations as cb

def prime_number(n:int):
    if n<=1:
        return False
    elif n==2:
        return True
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True


def solution(nums):
    answer=0
    for c in cb(nums,3):
        s=sum(c)
        if prime_number(s)==True:
            answer+=1

    return answer
