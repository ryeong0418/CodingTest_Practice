def solution(s):
    stack = []

    for x in s:
        if x == "#":
            stack.pop()
        else:
            stack.append(x)

    answer = ''.join(stack)
    return answer


print(solution("abc##ec#ab"))
print(solution("kefd#ef##s##"))
print(solution("teac#cher##er"))
print(solution("englitk##shabcde##ff##ef##ashe####"))
print(solution("itistime####gold"))
