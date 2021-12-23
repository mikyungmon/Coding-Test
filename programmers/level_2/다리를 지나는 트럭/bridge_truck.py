def solution(bridge_length, weight, truck_weights):
    seconds = 0
    bridge_len = [0 for i in range(bridge_length)]   # 다리 길이만큼 list 생성

    while truck_weights:
        seconds += 1
        bridge_len.pop(0)   # pop : 지정한 위치 값을 삭제 후 반환
        if (truck_weights[0] + sum(bridge_len)) <= weight:
            bridge_len.append(truck_weights.pop(0))
        else:
            bridge_len.append(0)

    return seconds + bridge_length