

# Please write your code here.

A = input()
def is_palindrome(A):
    if A == A[::-1]: 
        print('Yes')
    else:
        print('No')

is_palindrome(A)