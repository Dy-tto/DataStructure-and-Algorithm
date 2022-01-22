def solution(id_list, report, k):
    answer=[0] * len(id_list)
    set_repo=set(report)
    reports={x:0 for x in id_list}
    for i in set_repo:
        reports[i.split()[1]]+=1
    for j in set_repo:
        if reports[j.split()[1]]>=k:
            answer[id_list.index(j.split()[0])]+=1
    
    return answer
