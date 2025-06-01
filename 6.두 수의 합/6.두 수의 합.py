def solution(num1, num2):
    answer = -1
    if 0>num1 or 100<num1:
        print("잘못된 수")
    else:
        if 0>num2 or 100<num2:
            print("잘못된 수")
        else:
            answer=int((num1/num2)*1000)
    return answer