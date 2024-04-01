def solution(nums):

    unique_list = []

    for i in nums:
        if i not in unique_list:
            unique_list.append(i)

    for i in range(len(unique_list)):

        for j in range(i+1, len(unique_list)):

            if unique_list[i] < unique_list[j]:
                small_num = unique_list[i]
                big_num = unique_list[j]

                unique_list[i] = big_num
                unique_list[j] = small_num

    return unique_list


print(solution([0,1,1,1,2,2,2,3]))
print(solution([1,1,2,2,2,3,3,3,3,3,4,4,4,5]))
print(solution([0,0,0,3,3,3,5,7,7,7]))
print(solution([1,2,3,4,5,6,7,7,7,8,9]))