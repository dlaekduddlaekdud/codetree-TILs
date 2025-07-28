n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
def process_sequence(A, m):
    result = 0
    while m != 1:
        result += A[m - 1]
        if m % 2 == 0:
            m //= 2
        else:
            m -= 1
    result += A[0]  
    return result

print(process_sequence(A, m))
