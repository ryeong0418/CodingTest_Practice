
def solution(nums):

    answer = 1000
    num_list = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if answer >= abs(nums[i] - nums[j]):
                answer = abs(nums[i]-nums[j])

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if answer == abs(nums[i]-nums[j]):
                num_list.append([nums[i], nums[j]])

    return num_list


print(solution([3,8,1,5,12]))
print(solution([2,1,3,5,4]))
print(solution([5,10,15,20,25,11]))
print(solution([2,4,3,1,5,7,8,12,13,15,23]))
print(solution([100,200,300,400,120,130,135,132,121]))