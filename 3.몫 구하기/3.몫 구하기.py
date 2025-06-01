def solution(age):
    answer = 0
    if age>120:
        print('나이 120 이상')
    elif age<0:
        print('나이 0이하 입력')
    else:
        answer = 2022-age+1
    return answer