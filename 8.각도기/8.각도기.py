def solution(n):
    answer = 0
    if 0<n<=1000:
        for n in range(n+1):
            if n%2==0:
                answer+=n
    else :
        print("잘못된 값 입력")
    return answer

# for문에서 범위 설정하는 법을 몰라 알아봐서 range()를 사용,range는 0부터 작동하기때문에 원하는 값에 +1을 했다 #