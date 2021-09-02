def solution(numbers, hand):
    answer = ''
    left = 10
    right = 12

    for number in numbers:
        if number in [1, 4, 7]:
            answer += "L"
            left = number
        elif number in [3, 6, 9]:
            answer += "R"
            right = number
        else:
            number = 11 if number == 0 else number

            absL = abs(number - left)
            absR = abs(number - right)

            if sum(divmod(absL, 3)) > sum(divmod(absR, 3)):
                answer += "R"
                right = number
            elif sum(divmod(absL, 3)) < sum(divmod(absR, 3)):
                answer += "L"
                left = number
            else:
                if hand == "left":
                    answer += "L"
                    left = number
                else:
                    answer += "R"
                    right = number

    return answer