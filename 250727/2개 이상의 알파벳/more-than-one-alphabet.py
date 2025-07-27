A = input()

# Please write your code here.
def is_valid(A):
    if len(set(A)) >= 2:
        print('Yes')
    else:
        print('No')

is_valid(A)