a, b, c = map(int, input().split())
print(min(a, b, c))

# min 함수 사용할 수 없을 때
def get_min(a, b, c):
    min_val = a
    if min_val > b:
        min_val = b
    if min_val > c:
        min_val = c

    return min_val


print(get_min(a, b, c))