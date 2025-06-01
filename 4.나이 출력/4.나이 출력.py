def solution(num1, num2):
    answer = 0
    if 0>num1 or 10000<num1:
        print("XXXXX")
    else:
        if 0>num2 or 10000<num2:
            print("XXXXX")
        else:
            if num1==num2:
                answer=1
            else:
                answer=-1
    print(answer)
    return answer