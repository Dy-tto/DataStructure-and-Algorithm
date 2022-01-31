# 이코테 이진 탐색
# 정렬된 배열에서 특정 수의 개수 구하기

from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(lst, left_value, right_value):
    right_index=bisect_right(lst,right_value)
    left_index=bisect_left(lst,left_value)

    return right_index - left_index

# 데이터의 개수 n, 찾고자 하는 값 x 입력
n,x=map(int,input().split())
# 전체 데이터 입력
lst=list(map(int,input().split()))
lst.sort()
# 값이 [x,x] 범위에 있는 데이터의 개수 계산
count=count_by_range(lst,x,x)

if count==0:
    print(-1)
else:
    print(count)
