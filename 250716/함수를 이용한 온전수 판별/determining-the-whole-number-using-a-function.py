a, b = map(int, input().split())

# Please write your code here.
def f(a, b):
    count = 0

    for n in range(a, b + 1):
        if n % 2 == 0 or n % 10 == 5 or (n % 3 == 0 and n % 9 != 0):
            continue
        count += 1
    return count

print(f(a, b))