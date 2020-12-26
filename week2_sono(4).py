
N = input("99이하의 양의 정수 N을 입력해 주세요 : ")
while (0 > int(N)) or (99 < int(N)):
    N = input("음수거나 100이상의 수에요 ㅋㅋㅋ 수학 개념 무엇..? ^^.99이하의 양의 정수 N을 입력해 주세요 :")

outcome, cnt = N, 0

if len(N) == 1:
    outcome += "0"
    N += "0"

while True:
    outcome= outcome[-1] + str(int(outcome[0]) + int(outcome[1]))[-1]
    cnt += 1
    if outcome == N:
        break

print(cnt)