def solution(price, money, count):
    use_money = 0    # 사용해야되는 돈
    for i in range(1, count + 1):
        use_money += price * i

    if use_money >= money:
        answer = use_money - money
        return answer
    else:   # 주의! 부족하지 않을 때 0을 return !
        return 0