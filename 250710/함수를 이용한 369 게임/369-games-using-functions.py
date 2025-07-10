

def f(a, b):
    count = 0
    for n in range(a, b + 1):
        digits = list(str(n))
        if '3' in digits or '6' in digits or '9' in digits or n % 3 == 0:
            count += 1
    return count


a, b = map(int, input().split())
print(f(a,b))