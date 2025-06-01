def solution(num1, num2):
    answer = -1
    if -50000>num1 or 50000<num1:
        print("잘못된 수")
    else:
        if -50000>num2 or 50000<num2:
            print("잘못된 수")
        else:
            answer=num1+num2
    return answer