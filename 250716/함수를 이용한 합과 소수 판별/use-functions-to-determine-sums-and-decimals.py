a, b = map(int, input().split())
count = 0

for n in range(a, b + 1):
    # 소수 판별
    if n < 2:
        continue
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    if not is_prime:
        continue

    # 자릿수 합이 짝수인지 확인
    digit_sum = sum(int(d) for d in str(n))
    if digit_sum % 2 == 0:
        count += 1

print(count)
