a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.
def add(a, c):
    return(f'{a} + {c} = {a + c}') 

def sub(a, c):
    return(f'{a} - {c} = {a - c}') 

def div(a, c):
    return(f'{a} / {c} = {a // c}') 

def mul(a, c):
    return(f'{a} * {c} = {a * c}') 

if o == '+':
    print(add(a, c))
elif o == '-':
    print(sub(a, c))
elif o == '/':
    print(div(a, c))
elif o == '*':
    print(mul(a, c))
else :
    print('False')
