def solution(angle):
    answer = 0
    if 0 < angle <= 180:
        if angle < 90:
            answer = 1
        elif angle == 90:
            answer = 2
        elif angle < 180:
            answer = 3
        else:
            answer = 4
    else:
        print("잘못된 각도")

    return answer