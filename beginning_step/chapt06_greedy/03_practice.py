
def solution(nums, m):

    nums.sort(key=lambda v:v[0])
    print(nums, len(nums))
    nums_value_list = []
    max_value = 0
    max_value_2 = 0

    for i in range(len(nums)):
        if nums[i][0] == 0:
            print(nums[i])
            max_value = max(max_value, nums[i][1])

        elif nums[i][0]<=max_value and nums[i][1]>max_value:
            print(f'max_value: {max_value}')
            max_value_2 = max(max_value_2, nums[i][1])

    print(max_value)
    print(max_value_2)

print(solution([[5,10],[1,8],[0,2],[0,3],[2,5],[2,6],[10,12],[7,12]],12))