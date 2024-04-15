
def solution(home):

    if home%5 == 0:
        return home//5

    if home%5 != 0:

        if home%5 == 1 or home%5 == 2 or home%5 == 3:
            return home//5+home%5

        elif home%5 == 4:
            return (home//5)+2


print(solution(10))
print(solution(14))
print(solution(25))
print(solution(24))
print(solution(345))