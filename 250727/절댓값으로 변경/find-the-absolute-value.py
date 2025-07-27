n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def absolute_value(arr):
    for i in arr:
        if i > 0:
            print(i, end = ' ')
        else:
            print(-i, end = ' ')

absolute_value(arr)
