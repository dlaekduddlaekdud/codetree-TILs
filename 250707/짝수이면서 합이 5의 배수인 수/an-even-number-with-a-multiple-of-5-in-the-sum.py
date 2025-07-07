def check_number(n):
    digits = list(str(n))
    digit_sum = int(digits[0]) + int(digits[1])

    if n % 2 == 0 and digit_sum % 5 == 0:
        print('Yes')
    else:
        print('No')  

n = int(input())
check_number(n)