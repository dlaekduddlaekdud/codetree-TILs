a, b, c = 5, 6, 7

# 중간 변수 temp를 사용하여 순서대로 값을 교환
temp = b  # temp에 b의 값(6)을 저장
b = a     # b에 a의 값(5)을 대입
c = temp  # c에 temp(6)을 대입
a = 7     # a에 c의 이전 값(7)을 직접 대입

print(a)  
print(b)  
print(c)