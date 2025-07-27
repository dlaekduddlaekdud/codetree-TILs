a, b = map(int, input().split())

# Please write your code here.

def f(a, b):
    if a > b:
        a *= 2
        b += 10
        print(a, b)
    else:
        b *= 2
        a += 10
        print(a, b)

f(a, b)