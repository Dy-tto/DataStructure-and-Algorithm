def solution(lottos, win_nums):
    answer = []
    count=0
    zero_num=lottos.count(0)

    for i in lottos:
        if i in win_nums:
            count+=1
    best=7-(count+zero_num)
    worst=7-count
    if best>=6:
        best=6
    if worst>=6:
        worst=6
    answer.append(best)
    answer.append(worst)

    return answer
