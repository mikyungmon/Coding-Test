# or 앞이 참일경우 해당 값까지만 , 거짓일경우 뒤에 것까지 호출
# sort랑 sorted차이는 원래 리스트 자체를 바꾸는지 아닌지(sort는 원래 배열도 바꿔버림, sorted는 원래 배열은 그대로)
def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]