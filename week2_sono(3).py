# 첫째줄에 import random 을 입력해주세요
# 리스트 a에 들어갈 각각의 정수는 random.randrange(0, 100 + 1)로 추가시켜주세요.

# 입력
# input을 이용하여 한 줄에 N, X를 입력한다.

# 출력
# X보다 작은 수를 순서대로 공백으로 구분해 출력한다.

# 조건
# 존재할 수 있는 리스트는 오직 a뿐입니다. 다른 리스트를 생성하지 말아주세요.

# input_example
# N, X = 10, 5
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# output_example
# 1 2 3 4

import random

N, X = input().split()

a = []
for i in range(int(N)):
    ran = random.randrange(0, 100 + 1)
    a.append(ran)
    if ran < int(X):
        print(ran, end=' ')

print("\n",a)
