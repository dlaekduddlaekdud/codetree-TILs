a, b = map(int, input().split())

# Please write your code here.
def f(a, b):
    total = 0
    for n in range(a, b + 1):
        for i in range(2, n):
            if n % i == 0 :
                break
        else:
            total += n
    return total

print(f(a,b))   