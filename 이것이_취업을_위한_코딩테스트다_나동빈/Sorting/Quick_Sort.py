# Quick Sort

lst=[5,7,9,0,3,1,6,2,4,8]

def quick_sort(lst:list):
    if len(lst)<=1:
        return lst
    pivot=lst[0]
    tail=lst[1:]

    left=[x for x in tail if x<=pivot] # 분할된 왼쪽 부분
    right=[x for x in tail if x>pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left) + [pivot] + quick_sort(right)
print(quick_sort(lst))
