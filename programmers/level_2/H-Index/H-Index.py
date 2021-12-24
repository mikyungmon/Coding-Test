def solution(citations):
    a = []
    citations.sort(reverse=True)   # 큰 수 -> 작은 수 순서대로 정렬
    for i in range(1,len(citations)+1):
        if citations[i-1] >= i:
            a.append(i)
    return len(a)

# 알고리즘 순서
# 1. 큰 값->작은 값 순서대로 정렬하기
# 2. 위치(인덱스 값 + 1)보다 리스트 값이 크거나 같은 마지막 위치 찾아서 그 값 반환 => 이게 h값 의미