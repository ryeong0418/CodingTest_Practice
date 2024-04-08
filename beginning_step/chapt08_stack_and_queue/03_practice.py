def solution(s):
    stack = []

    for i in range(len(s)):
        if len(stack) > 0:
            if s[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
        else:
            stack.append(s[i])

    return ''.join(stack)


print(solution('acbbcaa'))
print(solution('bacccaba'))
print(solution('aabaababbaa'))
print(solution('bcaacccbaabccabbaa'))
print(solution('cacaabbc'))