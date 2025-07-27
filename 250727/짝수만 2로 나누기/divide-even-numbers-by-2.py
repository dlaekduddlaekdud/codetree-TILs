
# Please write your code here.

def divide_even(arr):
    for i in arr:
        if i % 2 == 0:
            print(i //2, end = ' ')
        else:
            print(i, end = ' ')

n = int(input())
arr = list(map(int, input().split()))

divide_even(arr)