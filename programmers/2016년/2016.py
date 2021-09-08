def solution(a, b):  # a - month, b - day
    month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    pre_month = []  # a = 5이면 1,2,3,4월 담은 list
    month_day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_day = 0
    week = 0
    week_name = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']

    for j in range(0, 12):
        if a > month[j]:
            pre_month.append(month[j])

    for k in range(len(pre_month)):
        total_day += month_day[pre_month[k] - 1]

    total_day += b

    week = total_day % 7

    return week_name[week - 1]