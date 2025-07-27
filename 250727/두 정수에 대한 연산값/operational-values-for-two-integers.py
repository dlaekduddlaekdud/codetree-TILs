a, b = map(int, input().split())

# Please write your code here.

if a > b:
    a += 25
    b *= 2
    print(a, b)

else:
    b += 25
    a *= 2
    print(a, b)