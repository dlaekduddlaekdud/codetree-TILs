n, m = map(int, input().split())
gcd = 1
# Please write your code here.

for i in range(1, m + 1):   
    if n % i == 0 and m % i == 0:
        gcd = i

print(gcd)
