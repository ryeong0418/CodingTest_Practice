
def solution(nums):

    answer = 0
    answer_list=[]
    long_answer = 0

    for i in range(len(nums)):

        if nums[i] == 1:
            answer += 1

        else:
            answer_list.append(answer)
            answer = 0

    answer_list.append(answer)

    for i in answer_list:
        if long_answer < i:
            long_answer = i

    return long_answer

print(solution([1,1,0,1,1,1,0,1,1,1,1,1]))
print(solution([0,0,1,0,1,0,0]))
print(solution([1,1,1,1,1]))
print(solution([1,0,1,1,0,1,1,1,0,1,1,1,0,1]))
