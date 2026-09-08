N, M = map(int, input().split())

result = []

def backtracking(start):

    if len(result) == M:
        print(*result)
        return

    # start부터 N까지 하나씩 선택
    for i in range(start, N + 1):
        result.append(i)          # 숫자 선택
        backtracking(i + 1)       # 다음 숫자는 i보다 큰 숫자부터
        result.pop()              # 방금 선택한 숫자 취소

backtracking(1)