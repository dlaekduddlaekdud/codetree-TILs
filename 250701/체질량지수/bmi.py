h, w = map(int, input().split())
b = (w * 10000) / (h * h)
print(int(b))

if b > 25:
    print("Obesity")