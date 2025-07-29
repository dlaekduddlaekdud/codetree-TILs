n = int(input())

def print_(n):
    if n == 0:
        return
    print("HelloWorld")
    print_(n - 1)

print_(n)
