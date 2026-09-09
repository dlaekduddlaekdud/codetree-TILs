n = int(input())
count = 0

for i in range(n):
    scores = list(map(int, input().split()))
    avg = sum(scores)/ 4
    if avg >= 60:
        print("pass")
        count += 1
    else:
        print("fail")
print(count)
