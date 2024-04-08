def solution(nums):
    stack = []
    answer = 0

    for i in range(len(nums)):
        stack.append(nums[i])

        if len(stack) >= 3:

            if stack[-1] == 1 and stack[-2] == 2 and stack[-3] == 1:
                stack.pop()
                stack.pop()
                stack.pop()
                answer += 1

    return answer


print(solution([1,1,1,2,1,1,2,1,2,1]))
print(solution([2,1,1,2,1,1,2,1,1,1,2,1,2,1,1,2,1,2,1,2,1]))
print(solution([1,1,1,1,1,2,1,2,1,1,1]))
print(solution([2,1,1,1,2,1,2]))
print(solution([1,1,1,1,1,1,1]))
