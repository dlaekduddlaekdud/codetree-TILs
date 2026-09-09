nums = list(map(int, input().split()))
arr = []
count = 0 
total = 0

for n in nums:
    if n == 0:
        break
    arr.append(n)
    count += 1

for i in range(len(arr)):
    total += arr[i]
avg = total / count
print(total, f"{avg:.1f}")