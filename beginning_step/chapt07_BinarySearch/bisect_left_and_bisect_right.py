from bisect import bisect_left, bisect_right


def solution(nums, weight):

    left_answer = bisect_left(nums, weight) # nums 배열에서 weight보다 크거나 같은 값들 중에서 가장 작은 것을 찾아준다.
    right_answer = bisect_right(nums, weight) # nums 배열에서 weight보다 큰 것들 중에서 가장 작은 것을 찾아준다.
    return left_answer, right_answer


print(solution([70,80,80,80,80,90,90,90],80))
print(solution([70,80,80,80,80,90,90,90],90)) # 90보다 큰 인덱스는 없으므로, 가장 마지막 인덱스(len(nums))가 출력된다.