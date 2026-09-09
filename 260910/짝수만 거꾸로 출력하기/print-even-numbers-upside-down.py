n = int(input())
nums = list(map(int, input().split()))

# nums를 뒤에서부터 하나씩 확인
for num in reversed(nums):
    # 짝수라면 출력
    if num % 2 == 0:
        print(num, end=" ")