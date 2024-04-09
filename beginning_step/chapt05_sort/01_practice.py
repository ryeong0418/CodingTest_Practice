

def solution(nums):

    new_list = []
    for i in range(len(nums)):
        if nums[i] not in new_list:
            new_list.append(nums[i])

    if len(new_list) > len(nums)/2:
        return int(len(nums)/2)
    else:
        return int(len(new_list))


print(solution([2,1,1,3,2,3,1,2]))
print(solution([1,3,5,7,2,3,7,5,3,2,5,7,9,12]))
print(solution([5,5,5,5,5,5]))
print(solution([12,23,11,3,5,23,23,23,23,23,23,23]))
print(solution([100,200,300,400,500,600,700,800]))