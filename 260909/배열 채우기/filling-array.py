nums = list(map(int, input().split()))
arr = []
for n in nums :
    if n == 0:
        break
    arr.append(n)

for i in range(len(arr) - 1, -1, -1):
    print(arr[i], end = " ")