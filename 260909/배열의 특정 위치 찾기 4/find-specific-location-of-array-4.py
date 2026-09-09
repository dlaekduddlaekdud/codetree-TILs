nums = list(map(int, input().split()))
arr = []
even_count = 0
total = 0 

for n in nums:
    if n == 0:
        break
    elif n % 2 == 0 :
        even_count += 1
        total += n
    
print(even_count, total)
        